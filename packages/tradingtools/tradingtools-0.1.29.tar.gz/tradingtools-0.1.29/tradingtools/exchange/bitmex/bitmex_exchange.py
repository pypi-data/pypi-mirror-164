# -*- coding: utf-8 -*-

from __future__ import annotations

import logging
from typing import Dict, List

from tenacity import retry
from tenacity import retry_if_exception_type
from tenacity import stop_after_attempt
from tenacity import wait_exponential
import ccxt
import pandas as pd

from tradingtools.exchange.abc import ABCExchange
from tradingtools.util import to_nearest
from .bitmex_response_mapper import BitmexResponseMapper

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

__all__ = ['BitmexExchange']


class BitmexExchange(ABCExchange):
    name = 'bitmex'
    default_currency = "XBt"
    mapper = BitmexResponseMapper

    @property
    def base_rest_url(self) -> str:
        if self.test:
            return 'https://testnet.bitmex.com/api/v1'
        return 'https://bitmex.com/api/v1'

    @property
    def base_wss_url(self) -> str:
        if self.test:
            return 'wss://testnet.bitmex.com/ws'
        return 'wss://bitmex.com/ws'

    def cancel_order(self, order_id, params={}, *args, **kwargs) -> str:
        try:
            response = self.ccxt_obj.cancel_order(order_id, params=params)
        except Exception:
            raise

        return response

    def cancel_orders(self, symbol=None, params={}) -> dict:
        if symbol:
            symbol = self.get_real_symbol(symbol)
        try:
            response = self.ccxt_obj.cancel_all_orders(
                symbol=symbol,
                params=params,
            )
        except Exception:
            raise

        return response

    def close_position(self, symbol) -> dict:
        positions = self.get_positions(symbol)
        position = None
        for p in positions:
            if p['symbol'] == symbol:
                position = p
                break
        if position is None:
            raise ValueError('No position to close')

        side = 'buy' if position['side'] == 'sell' else 'sell'

        order = self.post_order(
            position['symbol'],
            'market',
            side,
            abs(position['size']),
            reduce_only=True,
        )

        return order

    def close_positions(self) -> List[dict]:
        positions = self.get_positions()

        orders = []
        for p in positions:
            side = 'buy' if p['side'] == 'sell' else 'sell'
            order = self.post_order(
                p['symbol'],
                'market',
                side,
                abs(p['size']),
                reduce_only=True,
            )
            orders.append(order)

        return orders

    def get_ohlcv_parameters(
        self,
        start,
        end,
        limit,
        symbol,
        timeframe,
        tf_len,
        tf_format,
        partial,
    ):
        symbol = self.get_real_symbol(symbol)

        start = pd.to_datetime(start) + pd.Timedelta(timeframe)
        start = start.strftime(tf_format)

        start_time = pd.to_datetime(start)
        end_time = pd.to_datetime(end)
        start_time_key = 'startTime'
        end_time_key = 'endTime'
        params = {
            'reverse': False,
            'count': min(limit or 1000, 1000),
            start_time_key: start_time.strftime(tf_format),
            end_time_key: end_time.strftime(tf_format),
        }

        def start_time_conv(ts):
            res = pd.to_datetime(ts, unit='ms').strftime('%Y-%m-%d %H:%M:%S')

            return res

        def end_time_conv(ts):
            return params[end_time_key]

        return {
            'symbol': symbol,
            'start_time_key': start_time_key,
            'start_time_conv': start_time_conv,
            'end_time_key': end_time_key,
            'end_time_conv': end_time_conv,
            'params': params,
        }

    def get_open_order(self, order_id) -> dict:
        try:
            response = self.ccxt_obj.fetch_order(order_id)
        except ccxt.OrderNotFound:
            raise ValueError('Bitmex Order not found.')
        except Exception:
            raise

        order = self.mapper.map_order_response(response['info'])

        return order

    def get_open_orders(self, symbol=None) -> List[dict]:
        try:
            response = self.ccxt_obj.fetch_open_orders()
        except Exception:
            raise

        orders = []
        if symbol:
            symbol = self.get_real_symbol(symbol)
            orders = [
                self.mapper.map_order_response(r['info'])
                for r in response
                if get_real_symbol(r['info']['symbol']) == symbol
            ]
        else:
            orders = [
                self.mapper.map_order_response(r['info']) for r in response
            ]

        return orders

    def get_positions(self, collateral_symbol=None, round_pnl=8) -> List[dict]:
        if collateral_symbol and not isinstance(collateral_symbol, str):
            raise ValueError('collateral_symbol must be a string')

        if round_pnl < 0 or not isinstance(round_pnl, int):
            raise ValueError('round_pnl must be a positive integer')

        try:
            positions = self.ccxt_obj.private_get_position(
                {'filter': self.ccxt_obj.json({'isOpen': True})}
            )
        except Exception:
            raise

        if not positions:
            return []

        tickers = self.ccxt_obj.fetch_tickers()
        if collateral_symbol:
            collateral_symbol = self.get_real_symbol(collateral_symbol)
        positions = [
            self.mapper.map_get_positions_response(
                p,
                tickers,
                collateral_symbol=collateral_symbol,
                round_pnl=round_pnl,
            )
            for p in positions
        ]
        return positions

    def get_wallets(self) -> Dict[str, List[dict]]:
        try:
            wallets = self.ccxt_obj.fetchBalance()["info"]
            logger.info(f"get_wallets fetch balance: {wallets}")
        except Exception:
            raise

        account_wallets = {
            "main": [
                self.mapper.map_balance_response(wallet)
                for wallet in wallets
                if wallet["currency"].lower() == self.default_currency.lower()
            ]
        }
        return account_wallets

    def modify_order(
        self,
        order_id,
        price=None,
        size=None,
        trigger_price=None,
        trail_value=None,
    ) -> dict:
        symbol = self.get_real_symbol(self.get_open_order(order_id)['symbol'])
        market_info = self.markets[symbol]
        size_increment = market_info['info']['lotSize']
        price_increment = market_info['info']['tickSize']

        if size:
            size = to_nearest(size, size_increment)
        if price:
            price = to_nearest(price, price_increment)
        if trigger_price:
            trigger_price = to_nearest(trigger_price, price_increment)
        if trail_value:
            trail_value = to_nearest(trail_value, price_increment)

        params = {}

        if trigger_price:
            params['stopPx'] = trigger_price
        if trail_value:
            params['pegOffsetValue'] = trail_value

        response = self.ccxt_obj.edit_order(
            order_id, None, None, None, amount=size, price=price, params=params
        )

        order = self.mapper.map_order_response(response['info'])

        return order

    @retry(
        reraise=True,
        stop=stop_after_attempt(6),
        retry=retry_if_exception_type(ccxt.NetworkError),
        wait=wait_exponential(multiplier=1.5, max=30),
    )
    def post_order(
        self,
        symbol,
        order_type,
        side,
        size,
        price=None,
        post_only=False,
        reduce_only=False,
        trigger_price=None,
        trigger_price_type=None,
        close_on_trigger=False,
        trail_value=None,
        custom_order_id: str | None = None,
    ) -> dict:
        symbol = self.get_real_symbol(symbol)
        size_increment = self.size_inc(symbol)
        price_increment = self.price_inc(symbol)

        size = to_nearest(size, size_increment, round_down=True)

        if price:
            price = to_nearest(price, price_increment)
        if trigger_price:
            trigger_price = to_nearest(trigger_price, price_increment)
        if trail_value:
            trail_value = to_nearest(trail_value, price_increment)

        params = {}
        exec_inst_params = []

        if reduce_only is True:
            exec_inst_params.append('ReduceOnly')
        if post_only is True:
            exec_inst_params.append('ParticipateDoNotInitiate')
        if close_on_trigger is True:
            exec_inst_params.append('Close')
        if trigger_price_type and trigger_price_type != 'MarkPrice':
            exec_inst_params.append(trigger_price_type)
        if trail_value:
            params['pegOffsetValue'] = trail_value
            params['pegPriceType'] = 'TrailingStopPeg'
        if trigger_price:
            params['stopPx'] = trigger_price
        if custom_order_id:
            params["clOrdID"] = str(custom_order_id)

        if len(exec_inst_params):
            params['execInst'] = ','.join(exec_inst_params)

        try:
            response = self.ccxt_obj.create_order(
                symbol,
                order_type.title().replace('_', ''),
                side,
                size,
                price=price,
                params=params,
            )
        except Exception:
            raise

        order = self.mapper.map_order_response(response['info'])

        return order

    def size_inc(self, symbol):
        market_info = self.markets[self.get_real_symbol(symbol)]
        return market_info['info']['lotSize']

    def price_inc(self, symbol):
        market_info = self.markets[self.get_real_symbol(symbol)]
        return market_info['info']['tickSize']

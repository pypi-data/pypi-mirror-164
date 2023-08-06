"""Created by Lorenzo Cruz on November 24, 2021."""
from unittest.mock import patch

import pytest

from tradingtools.exchange import ExchangeFactory, BitmexExchange
from tradingtools.tests.mock_response import (
    MOCK_FETCH_BALANCE,
    MOCK_FETCH_BALANCE_MULTI_WALLET,
)


class TestExchangeBitmex:
    EXCHANGE = "bitmex"
    MOCK_API_KEY = "api_key"
    MOCK_API_SECRET = "api_secret"
    xbt_sats_mult = 0.00000001

    @pytest.fixture(autouse=True)
    def configure(self):
        self.exchange_factory = ExchangeFactory()
        self.exchange_factory.register_exchange(BitmexExchange)

    @pytest.mark.parametrize(
        "response",
        (MOCK_FETCH_BALANCE, MOCK_FETCH_BALANCE_MULTI_WALLET),
    )
    @patch(
        "tradingtools.exchange.bitmex.bitmex_exchange.ccxt.bitmex.fetch_balance"
    )
    @patch(
        "tradingtools.exchange.bitmex.bitmex_exchange.ccxt.bitmex.load_markets"
    )
    def test_get_wallets(self, load_markets, fetch_balance, response):
        load_markets.return_value = {}

        exchange = self.exchange_factory.get_exchange(
            exchange_name=self.EXCHANGE,
            api_key=self.MOCK_API_KEY,
            api_secret=self.MOCK_API_SECRET,
        )

        fetch_balance.return_value = response
        balance = next(
            wallet
            for wallet in response["info"]
            if wallet["currency"] == "XBt"
        )

        wallets = exchange.get_wallets()

        assert len(wallets["main"]) == 1

        assert wallets["main"][0]["asset"] == "BTC"
        assert (
            wallets["main"][0]["available"]
            == balance["availableMargin"] * self.xbt_sats_mult
        )
        assert (
            wallets["main"][0]["total"]
            == balance["walletBalance"] * self.xbt_sats_mult
        )

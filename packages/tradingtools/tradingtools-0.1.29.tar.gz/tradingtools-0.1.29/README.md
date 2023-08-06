# Trading Tools

See `requirements.txt` for the required 3rd-party Python packages used by this package.

# Installation

## Clone Repository

`git clone https://<username>@bitbucket.org/swapooquantitativedevelopment/trading-tools.git`

## Install the latest version of `pip`, `setuptools`, and `wheel`

`pip install --upgrade pip setuptools wheel`

## go to the repository root folder and install the `tradingtools` package

`pip install -e .`

# Exchange Subpackage

## Exchange Functions

* `cancel_order` - cancels the order posted to the exchange with the specified order ID
    * input
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key of the account with trade access
        * `api_secret` (`str`) - the API key of the account with trade access
        * `order_id` (`int`) - the ID of the order to be deleted
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        production API of the exchange
        * `*args` _(optional)_ - additional arguments that are implemented on an exchange method level
        * `**kwargs` _(optional)_ - additional keyword arguments that are implemented on an exchange method level
    * output
        * `str` - cancellation output message of exchange. The output can vary between different exchanges.

* `cancel_orders` - cancels the orders posted to the exchange with the specified market symbol
    * input
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key generated of the account with trade access
        * `api_secret` (`str`) - the API key generated of the account with trade access
        * `symbol` (`str`) - the symbol of the market in the exchange
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        production API of the exchange
        * `*args` _(optional)_ - additional arguments that are implemented on an exchange method level
        * `**kwargs` _(optional)_ - additional keyword arguments that are implemented on an exchange method level
    * output
        * `str` - cancellation output message of exchange. The output can vary between different exchanges.

* `cancel_orders_all_symbols` - cancels the orders posted to the exchange for all symbols
    * input
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key generated of the account with trade access
        * `api_secret` (`str`) - the API key generated of the account with trade access
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        production API of the exchange
        * `*args` _(optional)_ - additional arguments that are implemented on an exchange method level
        * `**kwargs` _(optional)_ - additional keyword arguments that are implemented on an exchange method level
    * output
        * `str` - cancellation output message of exchange. The output can vary between different exchanges.
        
* `close_position` - closes the position on the exchange with the given market symbol. The position is closed with a
market order.
    * input:
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key generated of the account with trade access
        * `api_secret` (`str`) - the API key generated of the account with trade access
        * `symbol` (`str`) - the symbol of the market in the exchange to close   
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        production API of the exchange
        * `*args` _(optional)_ - additional arguments that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional keyword arguments that are implemented on an exchange-specific level
    * output
        * `dict` - a dictionary containing the standardized output response of the exchange.
            * `created_at` (`str`) - the date when the order was created
            * `id` (`int`) - the order ID in the exchange
            * `symbol` (`str`) - the symbol of the position
            * `type` (`str`) - the order type executed
            * `side` (`str`) - the side of the order
            * `size` (`int`/`float`) - the size of the order
            * `price` (`int`/`float`) - the posted price of the order. limit orders only
            * `trigger_price` (`int`/`float`) - the trigger price of the order. for stop and take profit orders only
            * `filled_size` (`int`/`float`) - the filled orders on the exchange
            * `remaining_size` (`int`/`float`) - the remaining size to be filled by the order on the exchange
            * `status` (`str`) - the status of the order in the exchange
            * `reduce_only` (`bool`) - flag for determining if the order is reduce only
            * `ioc` (`bool`) - immediate or cancel
            * `post_only` (`bool`) - flag for determining if the order is post only
            * `retry_until_filled` (`bool`) - flag for determining if the order retries until filled

* `close_positions` - closes all the positions present in the exchange. The positions are closed with a market order.
    * input
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key generated of the account with trade access
        * `api_secret` (`str`) - the API key generated of the account with trade access
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        production API of the exchange
        * `*args` _(optional)_ - additional arguments that are implemented on an exchange method level
        * `**kwargs` _(optional)_ - additional keyword arguments that are implemented on an exchange method level
    * output
        * `list` of `dict` - a list dictionaries containing the standardized output responses from the exchange.
            * `created_at` (`str`) - the date when the order was created
            * `id` (`int`) - the order ID in the exchange
            * `symbol` (`str`) - the symbol of the position
            * `type` (`str`) - the order type executed
            * `side` (`str`) - the side of the order
            * `size` (`int`/`float`) - the size of the order
            * `price` (`int`/`float`) - the posted price of the order. limit orders only
            * `trigger_price` (`int`/`float`) - the trigger price of the order. for stop and take profit orders only
            * `filled_size` (`int`/`float`) - the filled orders on the exchange
            * `remaining_size` (`int`/`float`) - the remaining size to be filled by the order on the exchange
            * `status` (`str`) - the status of the order in the exchange
            * `reduce_only` (`bool`) - flag for determining if the order is reduce only
            * `ioc` (`bool`) - immediate or cancel
            * `post_only` (`bool`) - flag for determining if the order is post only
            * `retry_until_filled` (`bool`) - flag for determining if the order retries until filled

* `get_ohlcv` - fetches the historical OHLCV data of the symbol provided from the exchange
    * input
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `symbol` (`str`) - the symbol of the market in the exchange
        * `time_frame` (`str`) - the time frame of the OHLCV data
        * `start` (`datetime`) (optional) - the start date of the OHLCV data to be retrieved
        * `end` (`datetime`) (optional) - the end date of the OHLCV data to be retrieved
        * `limit` (`int`) (optional) - the number of OHLCV data to retrieve
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        live API of the exchange
        * `*args` _(optional)_ - additional args that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional kwargs that are implemented on an exchange-specific level
    * output
        * `pd.DataFrame` - the DataFrame object containing the OHLCV data fetched from the exchange.

* `get_open_order` - fetch the open order posted to the exchange given an order ID
    * parameters
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key of the account with read access
        * `api_secret` (`str`) - the API key of the account with read access
        * `order_id` (`int`) - the exchange order ID to be fetched
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        production API of the exchange
        * `*args` _(optional)_ - additional arguments that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional keyword arguments that are implemented on an exchange-specific level
    * output
        * `dict` - a dictionary containing the standardized output response of the exchange.
            * `created_at` (`str`) - the date when the order was created
            * `id` (`int`) - the order ID in the exchange
            * `symbol` (`str`) - the symbol of the position
            * `type` (`str`) - the order type executed
            * `side` (`str`) - the side of the order
            * `size` (`int`/`float`) - the size of the order
            * `price` (`int`/`float`) - the posted price of the order. limit orders only
            * `trigger_price` (`int`/`float`) - the trigger price of the order. for stop and take profit orders only
            * `filled_size` (`int`/`float`) - the filled orders on the exchange
            * `remaining_size` (`int`/`float`) - the remaining size to be filled by the order on the exchange
            * `status` (`str`) - the status of the order in the exchange
            * `reduce_only` (`bool`) - flag for determining if the order is reduce only
            * `ioc` (`bool`) - immediate or cancel
            * `post_only` (`bool`) - flag for determining if the order is post only
            * `retry_until_filled` (`bool`) - flag for determining if the order retries until filled

* `get_open_orders` - fetch the open order/s posted to the exchange given a symbol
    * parameters
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key of the account with read access
        * `api_secret` (`str`) - the API key of the account with read access
        * `symbol` (`int`) - the symbol orders to be fetched from the exchange
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        live API of the exchange
        * `*args` _(optional)_ - additional args that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional kwargs that are implemented on an exchange-specific level
    * output
        * `list` of `dict` - a list dictionaries containing the standardized output responses from the exchange.
            * `created_at` (`str`) - the date when the order was created
            * `id` (`int`) - the order ID in the exchange
            * `symbol` (`str`) - the symbol of the position
            * `type` (`str`) - the order type executed
            * `side` (`str`) - the side of the order
            * `size` (`int`/`float`) - the size of the order
            * `price` (`int`/`float`) - the posted price of the order. limit orders only
            * `trigger_price` (`int`/`float`) - the trigger price of the order. for stop and take profit orders only
            * `filled_size` (`int`/`float`) - the filled orders on the exchange
            * `remaining_size` (`int`/`float`) - the remaining size to be filled by the order on the exchange
            * `status` (`str`) - the status of the order in the exchange
            * `reduce_only` (`bool`) - flag for determining if the order is reduce only
            * `ioc` (`bool`) - immediate or cancel
            * `post_only` (`bool`) - flag for determining if the order is post only
            * `retry_until_filled` (`bool`) - flag for determining if the order retries until filled
      
* `get_open_orders_all_symbols` - fetch all open orders posted to the exchange
    * parameters
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key of the account with read access
        * `api_secret` (`str`) - the API key of the account with read access
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        live API of the exchange
        * `*args` _(optional)_ - additional args that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional kwargs that are implemented on an exchange-specific level
    * output
        * `list` of `dict` - a list dictionaries containing the standardized output responses from the exchange.
            * `created_at` (`str`) - the date when the order was created
            * `id` (`int`) - the order ID in the exchange
            * `symbol` (`str`) - the symbol of the position
            * `type` (`str`) - the order type executed
            * `side` (`str`) - the side of the order
            * `size` (`int`/`float`) - the size of the order
            * `price` (`int`/`float`) - the posted price of the order. limit orders only
            * `trigger_price` (`int`/`float`) - the trigger price of the order. for stop and take profit orders only
            * `filled_size` (`int`/`float`) - the filled orders on the exchange
            * `remaining_size` (`int`/`float`) - the remaining size to be filled by the order on the exchange
            * `status` (`str`) - the status of the order in the exchange
            * `reduce_only` (`bool`) - flag for determining if the order is reduce only
            * `ioc` (`bool`) - immediate or cancel
            * `post_only` (`bool`) - flag for determining if the order is post only
            * `retry_until_filled` (`bool`) - flag for determining if the order retries until filled

* `get_position` - fetch the open position from the exchange given a symbol
    * parameters
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key of the account with read access
        * `api_secret` (`str`) - the API key of the account with read access
        * `symbol` (`int`) - the position's symbol to be fetched from the exchange
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        production API of the exchange
        * `*args` _(optional)_ - additional arguments that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional keyword arguments that are implemented on an exchange-specific level
    * expected output
        * `dict` - a dictionary containing the standardized output from the exchange
            * `symbol` (`str`) - the symbol of the open position
            * `side` (`str`) - the side of the open position
            * `size` (`str`) - the size of the open position. positive if buy/long, negative if sell/short
            * `avg_price` (`int`/`float`) - the average price of the position
            * `unrealized_pnl` (`int`/`float`) - the unrealized pnl of the position
          
* `get_positions` - fetches the open positions from the exchange for all symbols
    * parameters
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key of the account with read access
        * `api_secret` (`str`) - the API key of the account with read access
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        live API of the exchange
        * `*args` _(optional)_ - additional args that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional kwargs that are implemented on an exchange-specific level
    * expected output
        * `list` of `dict` - a list of dictionaries containing the standardized output from the exchange
            * `symbol` (`str`) - the symbol of the open position
            * `side` (`str`) - the side of the open position
            * `size` (`str`) - the size of the open position. positive if buy/long, negative if sell/short
            * `avg_price` (`int`/`float`) - the average price of the position
            * `unrealized_pnl` (`int`/`float`) - the unrealized pnl of the position

* `get_wallets_balance` - fetches the wallets balance from the exchange for the account, including sub-accounts (if available)
    * parameters
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key of the account with read access
        * `api_secret` (`str`) - the API key of the account with read access
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        live API of the exchange
        * `*args` _(optional)_ - additional args that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional kwargs that are implemented on an exchange-specific level
    * expected output
        * `dict` - a dictionary containing the standardized output from the exchange
            * `key` (`str`) - the name of the account. Important feature for sub-accounts
            * `value` (`list`) - a `list` of `dict` containing the wallet balance for different coins
                * `asset` (`str`) - the symbol of the asset
                * `available` (`int`/`float`) - the number of available/usable balance
                * `total` (`int`/`float`) -the total balance of the asset

* `modify_order` - modifies an order's size or price based on the order ID provided
    * parameters
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key of the account with write/trade access
        * `api_secret` (`str`) - the API key of the account with write/trade access
        * `order_id` (`int`) - the ID of the order in the exchange to be modified
        * `size` (`int`/`float`) _(optional)_ - the new size of the order
        * `price` (`int`/`float`) _(optional)_ - the new price of the order
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        live API of the exchange
        * `*args` _(optional)_ - additional args that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional kwargs that are implemented on an exchange-specific level
    * output
        * `dict` - a dictionary containing the standardized output responses from the exchange.
            * `created_at` (`str`) - the date when the order was created
            * `id` (`int`) - the order ID in the exchange
            * `symbol` (`str`) - the symbol of the position
            * `type` (`str`) - the order type executed
            * `side` (`str`) - the side of the order
            * `size` (`int`/`float`) - the size of the order
            * `price` (`int`/`float`) - the posted price of the order. limit orders only
            * `trigger_price` (`int`/`float`) - the trigger price of the order. for stop and take profit orders only
            * `filled_size` (`int`/`float`) - the filled orders on the exchange
            * `remaining_size` (`int`/`float`) - the remaining size to be filled by the order on the exchange
            * `status` (`str`) - the status of the order in the exchange
            * `reduce_only` (`bool`) - flag for determining if the order is reduce only
            * `ioc` (`bool`) - immediate or cancel
            * `post_only` (`bool`) - flag for determining if the order is post only
            * `retry_until_filled` (`bool`) - flag for determining if the order retries until filled
          
* `post_order` - posts a new order to the exchange
    * parameters
        * `exchange_name` (`str`) - the name of the exchange to call the function with
        * `api_key` (`str`) - the API key of the account with write/trade access
        * `api_secret` (`str`) - the API key of the account with write/trade access
        * `order_type` (`str`) - the type of order to be posted to the exchange
        * `side` (`str`) - the side of order to be posted to the exchange
        * `size` (`int`/`float`) - the size of the order to be posted to the exchange
        * `price` (`int`/`float`) _(optional)_ - the price of the order to be posted to the exchange. Only used 
        by limit orders
        * `trigger_price` (`int`/`float`) _(optional)_ - the trigger price of the order to be posted to the exchange.
        Only used by certain types of orders like stop, and take profit.
        * `test` (`bool`) _(optional)_ - the flag that determines if the function will be using the testnet API or the 
        live API of the exchange
        * `*args` _(optional)_ - additional args that are implemented on an exchange-specific level
        * `**kwargs` _(optional)_ - additional kwargs that are implemented on an exchange-specific level
    * output
        * `dict` - a dictionary containing the standardized output responses from the exchange.
            * `created_at` (`str`) - the date when the order was created
            * `id` (`int`) - the order ID in the exchange
            * `symbol` (`str`) - the symbol of the position
            * `type` (`str`) - the order type executed
            * `side` (`str`) - the side of the order
            * `size` (`int`/`float`) - the size of the order
            * `price` (`int`/`float`) - the posted price of the order. limit orders only
            * `trigger_price` (`int`/`float`) - the trigger price of the order. for stop and take profit orders only
            * `filled_size` (`int`/`float`) - the filled orders on the exchange
            * `remaining_size` (`int`/`float`) - the remaining size to be filled by the order on the exchange
            * `status` (`str`) - the status of the order in the exchange
            * `reduce_only` (`bool`) - flag for determining if the order is reduce only
            * `ioc` (`bool`) - immediate or cancel
            * `post_only` (`bool`) - flag for determining if the order is post only
            * `retry_until_filled` (`bool`) - flag for determining if the order retries until filled

## Available Exchanges

* FTX

### FTX

For more information on the API, see https://docs.ftx.com/#overview.

#### Function Usage

##### `cancel_order`

```
from tradingtools.exchange import cancel_order


exchange = 'ftx'
api_key = 'YOUR-API-KEY'
api_secret = 'YOUR-API-SECRET'
order_id = 'ORDER-ID'

response = cancel_order(exchange, api_key, api_secret, order_id)
```

##### `cancel_orders`

```
from tradingtools.exchange import cancel_orders


exchange = 'ftx'
api_key = 'YOUR-API-KEY'
api_secret = 'YOUR-API-SECRET'
symbol = 'BTC-PERP'

conditional_orders_only = False # optional. cancels trigger orders only for symbol provided
limit_orders_only = False # optional. cancels limit orders only for symbol provided

# additional kwargs for the benefit of FTX specifically
# optional if you need these
params = {
    'conditionalOrdersOnly': conditional_orders_only,
    'limitOrdersOnly': limit_orders_only
}

# you can call the function like this
response = cancel_orders(exchange, api_key, api_secret, symbol, **params) # note **params, not params

# or you can call the function like this
response = cancel_orders(exchange, api_key, api_secret, symbol, conditionalOrdersOnly=conditional_orders_only, 
                         limitOrdersOnly=limit_orders_only)
```

##### `cancel_orders_all_symbols`

```
from tradingtools.exchange import cancel_orders_all_symbols


exchange = 'ftx'
api_key = 'YOUR-API-KEY'
api_secret = 'YOUR-API-SECRET'

conditional_orders_only = False # optional. cancels trigger orders only for symbol provided
limit_orders_only = False # optional. cancels limit orders only for symbol provided

# additional kwargs for the benefit of FTX specifically
# optional if you need these
params = {
    'conditionalOrdersOnly': conditional_orders_only,
    'limitOrdersOnly': limit_orders_only
}

# you can call the function like this
response = cancel_orders_all_symbols(exchange, api_key, api_secret, **params) # note **params, not params

# or you can call the function like this
response = cancel_orders_all_symbols(exchange, api_key, api_secret, conditionalOrdersOnly=conditional_orders_only, 
                                     limitOrdersOnly=limit_orders_only)
```

##### `close_position`

```
from tradingtools.exchange import close_position


exchange = 'ftx'
api_key = 'API-key'
api_secret = 'API-secret'
symbol = 'BTC-PERP'

response = close_position(exchange, api_key, api_secret, symbol)
```

##### `close_positions`

```
from tradingtools.exchange import close_positions


exchange = 'ftx'
api_key = 'API-key'
api_secret = 'API-secret'
symbol = 'BTC-PERP'

response = close_positions(exchange, api_key, api_secret)
```

##### `get_ohlcv`

```
import datetime

from tradingtools.exchange import get_ohlcv


exchange = 'ftx'
symbol = 'BTC-PERP'
time_frame = '1d'
start = datetime.datetime(2019, 1, 1) # optional
end = datetime.datetime(2020, 1, 1) # optional
limit = 100 # optional
response = get_ohlcv(exchange, symbol, time_frame, start=start, end=end, limit=limit)
```

##### `get_open_order`

```
from tradingtools.exchange import get_open_order


exchange = 'ftx'
api_key = 'API-KEY'
api_secret = 'API-SECRET'
order_id = 'ORDER-ID'

response = get_open_order(exchange, api_key, api_secret, order_id)
```

##### `get_open_orders`

```
from tradingtools.exchange import get_open_orders


exchange = 'ftx'
api_key = 'API-KEY'
api_secret = 'API-SECRET'
symbol = 'BTC-PERP'

response = get_open_orders(exchange, api_key, api_secret, symbol)
```

##### `get_open_orders_all_symbols`

```
from tradingtools.exchange import get_open_orders_all_symbols


exchange = 'ftx'
api_key = 'API-KEY'
api_secret = 'API-SECRET'

response = get_open_orders_all_symbols(exchange, api_key, api_secret)
```

##### `get_position`

```
from tradingtools.exchange import get_position


exchange = 'ftx'
api_key = '123'
api_secret = '123'
symbol = 'BTC-PERP'
collateral_symbol = 'BTC/USD'  # optional. used to calculate unrealized_pnl based on a different asset. None means USD.
round_pnl = 8  # optional. used to round off unrealized_pnl by specific number of decimal places. 8 means 8 decimal places.

response = get_position(exchange, api_key, api_secret, symbol, collateral_symbol=collateral_symbol, round_pnl=round_pnl)
```

##### `get_positions`

```
from tradingtools.exchange import get_positions


exchange = 'ftx'
api_key = '123'
api_secret = '123'
collateral_symbol = 'BTC/USD'  # optional. used to calculate unrealized_pnl based on a different asset. None means USD.
round_pnl = 8  # optional. used to round off unrealized_pnl by specific number of decimal places. 8 means 8 decimal places.

response = get_positions(exchange, api_key, api_secret, collateral_symbol=collateral_symbol, round_pnl=round_pnl)
```

##### `get_wallets_balance`

```
from tradingtools.exchange import get_wallets_balance


exchange = 'ftx'
api_key = '123'
api_secret = '123'
wallets = get_wallets_balance(exchange, api_key, api_secret)
```

##### `modify_order`

```
from tradingtools.exchange import modify_order

exchange = 'ftx'
api_key = 'API-KEY'
api_secret = 'API-SECRET'
order_id = 'ORDER-ID'
size = 1 # optional
price = 1 # optional

order_type = 'market' # required for FTX to specify what type of order it is

response = modify_order(exchange, api_key, api_secret, order_id, size=size, price=price, order_type=order_type)
```

##### `post_order`

```
from tradingtools.exchange import post_order


exchange = 'ftx'
api_key = 'API-KEY'
api_secret = 'API-SECRET'
symbol = 'BTC-PERP'
order_type = 'market'
side = 'buy'
size = 1
price = 1 # optional. only used by limit, stop limit and takeProfit limit orders. Ignored if market order placed
trigger_price = None # optional. required only if order type is stop or takeProfit

# to specify a stop limit/takeProfit order, change order_type to `stop`/`takeProfit` and define price
reduce_only = False # optional. used by all types of orders

# additional params specific to FTX
post_only = False # optional. used by all types of orders
ioc = False # optional. used by market or limit orders only. only define if market or limit
# retry_until_fulfilled = False # optional. used by stop, trailingStop, or takeProfit. only define if stop, trailingStop or takeProfit
# trail_value = 1 # required if order type is trailingStop

params = {
    'postOnly': post_only,
    'ioc': ioc,
    # 'retryUntilFulfilled': retry_until_fulfilled, # optional. used if order_type is stop, trailingStop, or takeProfit
    # 'trailValue': trail_value, # required if order_type is trailing stop
}
# you can call the function like this
response = post_order(exchange, api_key, api_secret, symbol, order_type, side, size, price=price, trigger_price=trigger_price, **params)

# or like this
response = post_order(exchange, api_key, api_secret, symbol, order_type, side, size, price=price, postOnly=post_only,
                      ioc=ioc)
```

# Contributing

The instructions below teach you how to contribute to the `tradingtools` package.

## Code Guidelines

Follow PEP-8 and use the `black` python package to standardized code structure.

## Extending the `tradingtools` Package

TODO

## Extending the `exchange` Sub-Package

Here are the ways in which you can extend the `exchange` sub-package:
* creating a new exchange wrapper package under the `exchange` sub-package
* implementing a new method of the new exchange wrapper under the `exchange` sub-package
* creating a new function for the `exchange` sub-package

### Design

To understand the design better, see
https://refactoring.guru/design-patterns/abstract-factory/python/example

### How to Create a New Exchange Wrapper Package

In this example, an exchange wrapper package called `newexchange` will be created.

#### Create a `newexchange` package under the `exchange` sub-package.

folder structure

```
tradingtools
|___ exchanges
     |___ newexchange # newly created subpackage
          |___ __init__.py # newly created file
     ...
...
```

#### Create `newexchange_exchange.py` module inside the `newexchange` subpackage.

folder structure

```
tradingtools
|___ exchange
     |___ newexchange
          |___ __init__.py
          |___ newexchange_exchange.py # new module
     ...
...
```
   
Note: the standard naming convention for new exchange classes will be `<exchange name>_exchange.py`.

#### implement the `NewExchangeExchange` class. here is a sample of what `newexchange_exchange.py` should look like

newexchange_exchange.py

```
# -*- coding: utf-8 -*-

from tradingtools.exchange.abc import ABCExchange

from tradingtools.exchange.abc.method import (
    ABCMethodCancelOrder,
    ABCMethodCancelOrders,
    ABCMethodCancelOrdersAllSymbols,
    ABCMethodClosePosition,
    ABCMethodClosePositions,
    ABCMethodGetOHLCV,
    ABCMethodGetOpenOrder,
    ABCMethodGetOpenOrders,
    ABCMethodGetOpenOrdersAllSymbols,
    ABCMethodGetPosition,
    ABCMethodGetPositions,
    ABCMethodModifyOrder,
    ABCMethodPostOrder,
)

__all__ = ['NewExchangeExchange']


class NewExchangeExchange(ABCExchange):
    name = 'newexchange'

    @property
    def base_rest_url(self) -> str:
        # if no test server, just return the same endpoint
        if self.test:
            return 'https://newexchange.com/api'
        return 'https://test.newexchange.com/api'

    @property
    def base_wss_url(self) -> str:
        # if no test server, just return the same endpoint
        if self.test:
            return 'wss://newexchange.com/ws'
        return 'wss://test.newexchange.com/ws'

    def cancel_order(self) -> ABCMethodCancelOrder:
        raise NotImplementedError

    def cancel_orders(self) -> ABCMethodCancelOrders:
        raise NotImplementedError

    def cancel_orders_all_symbols(self) -> ABCMethodCancelOrdersAllSymbols:
        raise NotImplementedError

    def close_position(self) -> ABCMethodClosePosition:
        raise NotImplementedError

    def close_positions(self) -> ABCMethodClosePositions:
        raise NotImplementedError

    def get_ohlcv(self) -> ABCMethodGetOHLCV:
        raise NotImplementedError

    def get_open_order(self) -> ABCMethodGetOpenOrder:
        raise NotImplementedError

    def get_open_orders(self) -> ABCMethodGetOpenOrders:
        raise NotImplementedError

    def get_open_orders_all_symbols(self) -> ABCMethodGetOpenOrdersAllSymbols:
        raise NotImplementedError

    def get_position(self) -> ABCMethodGetPosition:
        raise NotImplementedError

    def get_positions(self) -> ABCMethodGetPositions:
        raise NotImplementedError

    def modify_order(self) -> ABCMethodModifyOrder:
        raise NotImplementedError

    def post_order(self) -> ABCMethodPostOrder:
        raise NotImplementedError

```
   
Note: the methods defined above are from the inherited methods defined in `ABCExchange`. See Design
for more info.

#### (optional) Create and implement a module that contains authentication functions for the new exchange.
    
folder structure
    
```
tradingtools
|___ exchange
     |___ newexchange
          |___ __init__.py
          |___ newexchange_exchange.py
          |___ newexchange_authentication.py # authentication module
     ...
...
```

newexchange_authentication.py

``` 
# -*- coding: utf-8 -*-


def rest_authentication(...):
    ...

def wss_authentication(...):
    ...

```

#### Import the newly created class and authentication functions (if implemented) under the `newexchange` subpackage `__init__.py` file
    
folder structure

```
tradingtools
|___ exchange
     |___ newexchange
          |___ __init__.py # modify this file
          |___ newexchange_exchange.py
          |___ newexchange_authentication.py
     ...
...
```

`__init__.py`

```
# -*- coding: utf-8 -*-

from .newexchange_exchange import *
from .newexchange_authentication import * # add if implemented

```

#### Add the new exchange to the exchange factory in the `exchange_factory.py` module.

folder structure

```
tradingtools
|___ exchange
     |___ newexchange
          |___ __init__.py
          |___ newexchange_exchange.py
          |___ newexchange_authentication.py
     ...
     |___ exchange_factory.py # modify this file
...
```

exchange_factory.py

```
# -*- coding: utf-8 -*-

...
from tradingtools.exchange.newexchange import NewExchangeExchange # import the class you made
...
factory.register_exchange(NewExchangeExhange.name, NewExchangeExchange) # register the class you made

```

### How to Implement a Method That's Used With the Existing Functions of the `exchange` Sub-Package

Let's assume that you already have the `newexchange` package created and that you're going to
implement the get_position method of the new exchange `newexchange`

#### (optional) If this the first time you're implementing a method, create new package `method` inside the 
`newpackage` package

```
tradingtools
|___ exchange
     |___ newexchange
          |___ method # newly created package
               |___ __init__.py # turns method into a package
          ...
     ...
...
```

#### Create a module that would contain the logic for the get_position method inside the `method` sub-package under the `newexchange` sub-package. This is where the logic for getting the position/s from the exchange will be placed. See example below.
    
folder structure

```
tradingtools
|___ exchange
     |___ newexchange
          |___ method
               |___ __init__.py
               |___ newexchange_method_get_position.py # newly created module
               ...
          ...
     ...
...
```

`newexchange_method_get_position.py`

```
# -*- coding: utf-8 -*-

from tradingtools.exchange.abc.method import (
    ABCMethodGetPosition,
    ABCMethodGetPositions,
)

__all__ = ['NewExchangeMethodGetPosition', 'NewExchangeMethodGetPositions']


class NewExchangeMethodGetPosition(ABCMethodGetPosition):
    def get_position(self, api_key: str, api_secret: str, symbol: str, *args, **kwargs):
        # logic here


class NewExchangeMethodGetPositions(ABCMethodGetPositions):
    def get_positions(self, api_key: str, api_secret: str, *args, **kwargs) -> List[dict]:
        # logic here

```

#### Import the newly created classes from `newexchange_method_get_position` to the `__init__.py` of the `method` sub-package of the `newexchange` package.

folder structure

```
tradingtools
|___ exchange
     |___ newexchange
          |___ method
               |___ __init__.py # modify this file
               |___ newexchange_method_get_position.py
               ...
          ...
     ...
...
```

`__init__.py`

```
# -*- coding: utf-8 -*-

...
from .newexchange_method_get_position import *

```

#### Add the new implementation to the `NewExchangeExchange` class defined previously.

folder structure

```
tradingtools
|___ exchange
     |___ newexchange
          |___ method
               |___ __init__.py
               |___ newexchange_method_get_position.py
               ...
          |___ newexchange_exchange.py # modify this file
     ...
...
```
   
`newexchange_exchange.py`
   
```
# -*- coding: utf-8 -*-

...
from tradingtools.exchange.newexchange.method import (
    ...
    NewExchangeMethodGetPosition,
    NewExchangeMethodGetPositions,
    ...
)

...


class NewExchangeExchange(ABCExchange):
    ...

    def get_position(self) -> ABCMethodGetPosition:
        return NewExchangeMethodGetPosition(self.base_rest_url, self.base_wss_url)

    def get_positions(self) -> ABCMethodGetPositions:
        return NewExchangeMethodGetPositions(self.base_rest_url, self_base_wss_url)

    ...
```
   
### How to Implement a New Function in the `exchange` Sub-Package

#### Add the new function in `tradingtools/exchange/exchange_functions.py`

`exchange_functions.py`

```
...
__all__ = [
    ...
    'new_function',
]
...
def new_function(exchange_name, ..., test=False, *args, **kwargs):
    exchange = factory.get_exchange(exchange_name, test=test)
    method = exchange.new_function()
    return method.new_functions(..., *args, **kwargs)
```

#### Create an ABCMethod class that relates to the new function in `tradingtools/exchange/abc/method` and add it to the `__init__.py` file of the method subpackage.

`tradingtools/exchange/abc/method/abc_method_new_function.py` - new `py` file

```
# -*- coding: utf-8 -*-

import abc

from .abc_method import ABCMethod

__all__ = ['ABCMethodNewFunction']


class ABCMethodNewFunction(ABCMethod, abc.ABC):
    @abc.abstractmethod
    def new_function(..., *args, **kwargs):
        raise NotImplementedError

```

`tradingtools/exchange/abc/method/__init__.py`

```
...
from .abc_new_method_function.py import *
...
```

#### Add the new ABC method implementation to the `ABCExchange` class as a new method

`tradingtools/exchange/abc/abc_exchange.py`

```
from tradingtools.exchange.abc.method import (
    ...
    ABCMethodNewFunction
    ...
)


class ABCExchange(...):
    ...
    @abc.abstractmethod
    def new_function(self) -> ABCMethodNewFunction:
        raise NotImplementedError
```

#### Implement the underlying exchange methods if it's available

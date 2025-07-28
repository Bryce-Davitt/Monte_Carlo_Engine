import yfinance as yf


def get_underlying_price(ticker):
    """
    Fetch the current underlying asset price for the given ticker.
    Args:
        ticker (str): Ticker symbol (e.g., 'AAPL')
    Returns:
        float: Current price
    """
    stock = yf.Ticker(ticker)
    price = stock.history(period='1d')['Close'].iloc[-1]
    return float(price)


def get_option_expiries(ticker):
    """
    Fetch available option expiries for the given ticker.
    Args:
        ticker (str): Ticker symbol
    Returns:
        list of str: Expiry dates in 'YYYY-MM-DD' format
    """
    stock = yf.Ticker(ticker)
    return stock.options


def get_option_chain(ticker, expiry):
    """
    Fetch the option chain (calls and puts) for a given ticker and expiry.
    Args:
        ticker (str): Ticker symbol
        expiry (str): Expiry date in 'YYYY-MM-DD' format
    Returns:
        dict: {'calls': DataFrame, 'puts': DataFrame}
    """
    stock = yf.Ticker(ticker)
    opt_chain = stock.option_chain(expiry)
    return {'calls': opt_chain.calls, 'puts': opt_chain.puts} 
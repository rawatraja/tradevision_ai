from providers.factory import get_provider
from cache.cache import market_data
from utils.logger import logger


def get_market(symbol):
    """
    Returns market data for the requested symbol.
    """

    try:
        logger.info(f"Loading market data for {symbol}")

        provider = get_provider()

        market = market_data(provider, symbol)

        logger.info(f"Successfully loaded {symbol}")

        return market

    except Exception as e:
        logger.error(f"Failed to load market data for {symbol}: {e}")

        return {
            "symbol": symbol,
            "spot": "N/A",
            "change": 0,
            "change_percent": 0,
            "time": "Unavailable"
        }
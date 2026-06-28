import pandas as pd
from pandas import DataFrame

from cache.cache import option_chain
from providers.factory import get_provider
from utils.logger import logger


def get_option_chain(symbol: str) -> DataFrame:
    """
    Returns the option chain for the given symbol.
    """

    try:
        logger.info(f"Loading option chain for {symbol}")

        provider = get_provider()

        df = option_chain(provider, symbol)

        logger.info(f"Loaded {len(df)} option chain rows for {symbol}")

        return df

    except Exception:
        logger.exception(f"Failed to load option chain for {symbol}")

        return pd.DataFrame()
from config import DATA_PROVIDER

from providers.mock import MockProvider
from providers.nse import NSEProvider
from providers.broker import BrokerProvider


def get_provider():
    """
    Returns the configured market data provider.
    """

    if DATA_PROVIDER == "mock":
        return MockProvider()

    elif DATA_PROVIDER == "nse":
        return NSEProvider()

    elif DATA_PROVIDER == "broker":
        return BrokerProvider()

    raise ValueError(
        f"Unknown DATA_PROVIDER: {DATA_PROVIDER}"
    )
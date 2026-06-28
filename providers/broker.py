from providers.base import MarketDataProvider


class BrokerProvider(MarketDataProvider):

    def get_market_data(self, symbol):
        raise NotImplementedError(
            "BrokerProvider is not implemented yet."
        )

    def get_option_chain(self, symbol):
        raise NotImplementedError(
            "BrokerProvider is not implemented yet."
        )

    def get_expiry_list(self, symbol):
        raise NotImplementedError(
            "BrokerProvider is not implemented yet."
        )
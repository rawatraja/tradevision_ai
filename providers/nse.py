from providers.base import MarketDataProvider


class NSEProvider(MarketDataProvider):

    def get_market_data(self, symbol):
        raise NotImplementedError(
            "NSEProvider is not implemented yet."
        )

    def get_option_chain(self, symbol):
        raise NotImplementedError(
            "NSEProvider is not implemented yet."
        )

    def get_expiry_list(self, symbol):
        raise NotImplementedError(
            "NSEProvider is not implemented yet."
        )
from abc import ABC, abstractmethod


class MarketDataProvider(ABC):

    @abstractmethod
    def get_market_data(self, symbol):
        pass

    @abstractmethod
    def get_option_chain(self, symbol):
        pass

    @abstractmethod
    def get_expiry_list(self, symbol):
        pass
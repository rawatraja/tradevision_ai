import pandas as pd
from datetime import datetime

from providers.base import MarketDataProvider


class MockProvider(MarketDataProvider):

    def get_market_data(self, symbol):

        return {
            "symbol": symbol,
            "spot": 25124.50,
            "change": 126.25,
            "change_percent": 0.52,
            "time": datetime.now().strftime("%H:%M:%S")
        }

    def get_option_chain(self, symbol):

        return pd.DataFrame({

            "Strike":[24900,24950,25000,25050,25100],

            "CE OI":[120000,240000,360000,210000,160000],

            "PE OI":[150000,230000,420000,330000,180000]

        })

    def get_expiry_list(self, symbol):

        return [

            "02 Jul 2026",

            "09 Jul 2026",

            "30 Jul 2026"

        ]
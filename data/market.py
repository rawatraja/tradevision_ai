from datetime import datetime


def get_market_data(symbol):

    return {
        "symbol": symbol,
        "spot": 25124.35,
        "change": 125.20,
        "change_percent": 0.50,
        "time": datetime.now().strftime("%H:%M:%S")
    }
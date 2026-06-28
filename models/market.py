# models/market.py

from dataclasses import dataclass


@dataclass
class MarketData:
    symbol: str
    spot: float
    change: float
    change_percent: float
    time: str
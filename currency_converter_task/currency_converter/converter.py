"""
Python file to convert money.
"""
from fetcher import fetch_exchange_rate

def converter(base: str, target: str, amount: float = 1, mock: bool = False) -> float:
    """
    Convert a given amount from base currency.
    """
    rate = fetch_exchange_rate(base, target)
    converted = amount * rate

    print(f"{amount} {base} = {converted} {target}")
    return converted

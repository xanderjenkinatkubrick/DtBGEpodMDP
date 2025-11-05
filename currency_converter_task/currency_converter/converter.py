"""
Python file to convert money.
"""
from fetcher import fetch_exchange_rate
from logger_config import my_logger

logger = my_logger()

def converter(base: str, target: str, amount: float = 1, mock: bool = False) -> float|None:
    """
    Convert a given amount from base currency to target currency.
    Returns converted amount (float) or None on conversion failure
    """
    if amount <= 0:
        logger.warning("Negative amount supplied. Please input a positive number.")
        raise ValueError("Negative amount supplied. Please input a positive number.")

    rate = fetch_exchange_rate(base, target)
    if rate is None:
        logger.warning("Rate unavailable for conversion. Check spelling.")
        return None

    converted = amount * rate
    logger.info("Converted %(amount)s %(base)s to %(target)s")

    return converted

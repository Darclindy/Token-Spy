
from price.PriceModel import PriceModel
from typing import Dict


price_data: Dict[str, PriceModel] = dict() # symbol -> PriceModel

def get_price(symbol, timestamp):
    if (symbol in price_data):
        model = price_data[symbol]
        return round(model.get_price(timestamp), 3)
    else:
        model = PriceModel(symbol=symbol)
        price_data[symbol] = model
        return round(model.get_price(timestamp=timestamp), 3)

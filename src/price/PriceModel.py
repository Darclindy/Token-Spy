# todo 将币价的数据临时保存在这里，共整个区块链查询；
from sdk.cmc.crypto_currency.CryptoCurrency import CRYPTO_CURRENCY_API
import json



class PriceModel:
    
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.price_map = dict() # timestamp -> price


    def get_price(self, timestamp):
        if (timestamp in self.price_map.keys()):
            return self.price_map[timestamp]
        else:
            self.__fetch_price(timestamp)
            if (len(self.price_map.keys()) > 0):
                print(f"get price, timestamp={timestamp}, pricekey={list(self.price_map.keys())[0]}")

            if (timestamp in self.price_map.keys()):
                return self.price_map[timestamp]
            else:
                return 0
    
    def __fetch_price(self, timestamp):
        try:
            result = CRYPTO_CURRENCY_API.quotes_historical({
                    "symbol":self.symbol,    
                    "time_end":timestamp,
                    "count":1000,
                    "interval":"5m",
                    "aux":"price,is_active"
            })

            if (result["status"]["error_code"] == 0):
                self.__on_success(result["data"][self.symbol][0]["quotes"])
            else:
                self.__on_fail(result["status"])
        except Exception as e:
            self.__on_error(e)


    def __on_success(self, quotes):
        timestamp_to_price  = { item["timestamp"]: item["quote"]["USD"]["price"] for item in quotes }
        self.__merge_new_price(timestamp_to_price)
        pass

    def __on_error(self, e):
        print(f"fetch price error, type={type(e)}, message={str(e)}")

    def __on_fail(self, status):
        print("fetch price failed" + json.dumps(status))
    

    def __merge_new_price(self, new_price):
        self.price_map.update(new_price)
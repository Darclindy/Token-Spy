import Constant
import json
from requests import Session, request
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects



class CryptoCurrencyAPI:

    __baseUrl = Constant.CMC_URL
    __session = Session()
    __headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': Constant.CMC_API_KEY,
    }

    def airdrops(self, params={}, header={}):
        path = "/v1/cryptocurrency/airdrops"
        parameters = {

        }
        parameters.update(params)
        self.__headers.update(header)

        result = self.__get(path, parameters)
        return result

    def historical_OHLCV_v2(self, params={}, header={}):
        path = "/v2/cryptocurrency/ohlcv/historical"
        parameters = {
            'id':'1',
            'symbol':'BTC',
            'time_period':'daily',
            'count':10000,
        }

        parameters.update(params)
        self.__headers.update(header)

        result = self.__get(path, parameters)
        return result
    

    def listings_historical(self, params={}, header={}):
        path = "/v1/cryptocurrency/listings/historical"
        parameters = {
            'start':1,
            'limit':5000,
            'date':'2024-03-01T00:00:00.000Z'
        }

        parameters.update(params)
        self.__headers.update(header)

        result = self.__get(path, parameters)
        return result
    
    def quotes_historical(self, params={},header={}):
        path = "/v3/cryptocurrency/quotes/historical"
        parameters = {
            "symbol":"WIF",
            "count":1000,
            "interval":"5m"
        }

        parameters.update(params)
        self.__headers.update(header)
        return self.__get(path, parameters)
        

    def price_performance(self, params={},header={}):
        path = "/v2/cryptocurrency/price-performance-stats/latest"
        parameters = {
            "symbol":"WIF",
            "count":1000,
            "interval":"5m"
        }

        parameters.update(params)
        self.__headers.update(header)
        return self.__get(path, parameters)
    

    def __get(self, path, params):
        url = self.__baseUrl + path
        self.__session.headers.update(self.__headers)

        try:
            response = self.__session.get(url, params=params)
            data = json.loads(response.text)
            # print(data)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            return "{}"



CRYPTO_CURRENCY_API = CryptoCurrencyAPI()

from sdk.cmc.crypto_currency.CryptoCurrency import *



def on_success(data):
    return round(data[0]["quotes"][0]["quote"]["USD"]["price"], 3)

def on_error(status):
    if (status is None):
        print("Error, response None")
        return 0
    else:
        print(status)
        return 0


def fetch_price(symbol, timestamp):
    if ("ERROR" in symbol):
        return 0
    
    try:
        result = CRYPTO_CURRENCY_API.quotes_historical(params = {
                'symbol': symbol,
                "count":2,
                'time_end':timestamp
        })

        if (result == {}):
            return on_error(None)
        elif (result["status"]["error_code"] != 0):
            return on_error(result["status"])
        else:
            return on_success(result["data"][symbol])
    except:
        print(f"fetch price error, symbol={symbol}, timestamp=${timestamp}")
        return 0


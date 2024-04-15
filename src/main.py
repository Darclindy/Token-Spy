from sdk.cmc.crypto_currency.CryptoCurrency import CRYPTO_CURRENCY_API
from sdk.helius.Transaction import transaction_history_test
from dune_client.client import DuneClient
import Constant
import json



def main():
    result = CRYPTO_CURRENCY_API.quotes_historical(params={
        "symbol":"SLERF"
    })
    with open("output/output.json",'a') as fs:
        fs.write(json.dumps(result))
    print(result)


def test():
    print("hello token-spy, this is a setup test!!!")
    

def test_dune():
    client = DuneClient(api_key=Constant.DUNE_API_KEY)
    result = client.get_latest_result(3535049)
    print("Results", result.result.rows)


def test_cmc():
    result = CRYPTO_CURRENCY_API.quotes_historical(params={"symbol":"BTC"})
    print(result)

def test_helius():
    transaction_history_test()



if __name__ == "__main__":
    main()


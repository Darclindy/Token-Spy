from sdk.cmc.crypto_currency.CryptoCurrency import CRYPTO_CURRENCY_API
from sdk.cmc.crypto_currency.HistoryCurrencyPresenter import fetch_price
from sdk.helius.Transaction import *
from dune_client.client import DuneClient
from transaction.Transaction import TransactionModel
from transaction.Account import Account
from utils.excel.ExcelExporter import ExcelExporter
import Constant
import json



def main():
    result = CRYPTO_CURRENCY_API.quotes_historical(params={
        "symbol":"SLERF"
    })
    with open("output/output.json",'a') as fs:
        fs.write(json.dumps(result))
    print(result)

def test_transaction():
    signature = ["xof911A5xUMteYD4ibJrGJe29iMMyRS2LJABUvCrrwVRsFZmtH9iWyDWpDodtojNyrqY8bioX86oQ1Z7Dp8i9HK"]
    address = "5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9"
    # transaction = get_all_transaction(address = address)
    transaction = transaction_history_test(address = address)
    model = TransactionModel.parse_transfers(transaction, address)

    account = Account(address)
    account.add_model_list(model)
    ExcelExporter.export_account(account)

    print(account)
    
    # account.write_to_excel()


def test():
    print("hello token-spy, this is a setup test!!!")
    # get_all_transaction("F82BqR5GqmVkc1X58WsnEPeTqVAvgk3tAavtmpoiw7PM")
    test_transaction()
    

def test_dune():
    client = DuneClient(api_key=Constant.DUNE_API_KEY)
    result = client.get_latest_result(3535049)
    print("Results", result.result.rows)


def test_cmc():
    print(fetch_price("ETH", "2024-04-15T07:33:33.000Z"))
    # result = CRYPTO_CURRENCY_API.quotes_historical(params={
    #     "symbol":"ETH",            
    #     "time_end":"2024-04-15T07:33:33.000Z",
    #     "count":2,
    #     "interval":"5m",
    #     })
    
    # write_to_file(f"json/price/eth.json", json.dumps(result))

def test_helius():
    transaction_history_test(address = "F82BqR5GqmVkc1X58WsnEPeTqVAvgk3tAavtmpoiw7PM")
    # transaction_test()



if __name__ == "__main__":
    test_transaction()


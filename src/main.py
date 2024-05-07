from sdk.cmc.crypto_currency.CryptoCurrency import CRYPTO_CURRENCY_API
from sdk.cmc.crypto_currency.HistoryCurrencyPresenter import fetch_price
from sdk.helius.Transaction import *
from dune_client.client import DuneClient
from transaction.Transaction import TransactionModel
from transaction.Account import Account
from utils.excel.ExcelExporter import ExcelExporter
import Constant
import json
import numpy as np
import argparse




def main():
    result = CRYPTO_CURRENCY_API.quotes_historical(params={
        "symbol":"SLERF"
    })
    with open("output/output.json",'a') as fs:
        fs.write(json.dumps(result))
    print(result)

def test_transaction():
    np.set_printoptions(formatter={"float": ':0.8f'.format})

    signature = ["xof911A5xUMteYD4ibJrGJe29iMMyRS2LJABUvCrrwVRsFZmtH9iWyDWpDodtojNyrqY8bioX86oQ1Z7Dp8i9HK"]
    # address = "5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9"
    address = "Ew4uNiPvSDN2ioV1xbgjCVrAzVVM8873U1n3ZYwC5739"
    transaction = get_all_transaction(address = address)
    # transaction = transaction_history_test(address = address)
    model = TransactionModel.parse_transfers(transaction, address)

    account = Account(address)
    account.add_model_list(model)
    ExcelExporter.export_account(account)
    account.write_to_json()

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
    # print(fetch_price("ETH", "2024-04-15T07:33:33.000Z"))
    result = CRYPTO_CURRENCY_API.quotes_historical(params={
        "symbol":"ETH,BTC,SOL,CSV,BCH,BOME,SLERF",            
        # "time_end":"2024-04-15T07:33:33.000Z",
        "count":1000,
        "interval":"5m",
        "aux":"price"
        })
    
    write_to_file(f"json/price/multi_coin_price.json", json.dumps(result))

def test_helius():
    transaction_history_test(address = "Ew4uNiPvSDN2ioV1xbgjCVrAzVVM8873U1n3ZYwC5739")
    # transaction_test()

def address_analysis():
    parser = argparse.ArgumentParser()
    parser.add_argument("address", help="target account's address")
    parser.add_argument("-a", "--action", help="transaction type", choices=["transfer", "swap"], metavar="")
    parser.add_argument("-d", "--duration", help="time duration", choices=['1d', '2d', '3d', '7d', '14d', '1m', '2m', '3m', '6m', '1y'], metavar="")
    parser.add_argument("-ss", help="start signature")
    parser.add_argument("-es", help="end signature")

    args = parser.parse_args()

    address = args.address

    transaction = get_all_transaction(address = address)
    model = TransactionModel.parse_transfers(transaction, address)

    account = Account(address)
    account.add_model_list(model)
    ExcelExporter.export_account(account)
    account.write_to_json()
    print(account)


def profit_calculation():
    parser = argparse.ArgumentParser()
    parser.add_argument("address", help="target account's address")
    parser.add_argument("-a", "--action", help="transaction type", choices=["transfer", "swap"], metavar="")
    parser.add_argument("-p", "--path", help="transaction account path")

    print("profit_calculation function is comming soon..")



if __name__ == "__main__":
    test_transaction()


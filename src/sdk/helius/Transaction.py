
from helius import TransactionsAPI
from sdk.helius.Context import TransactionsAPI
from utils.out import *
import json


#目前会用到的 transaction_type
transaction_type = {"transfer":"TRANSFER", "swap": "SWAP"}

def transaction_test():
    transactions = ["WhEairASuHdDZp6pQJGBH85dCReskiCpHRFKSEKQh7wcBEBAHmAGcaDrBikJokH2B63xGLJrhvPMJfXpZuwJjqw"]
    raw_transactions = TransactionsAPI.get_parsed_transactions(transactions = transactions )
    write_to_file(f"output/json/transaction/{transactions[0]}.json", json.dumps(raw_transactions))

    print(raw_transactions)

def transaction_history_test():
    address = "F82BqR5GqmVkc1X58WsnEPeTqVAvgk3tAavtmpoiw7PM"
    parsed_transaction_history = TransactionsAPI.get_parsed_transaction_history(address=address, type=transaction_type.values())
    write_to_file(f"output/json/history/{address}.json", json.dumps(parsed_transaction_history))
    print(parsed_transaction_history)


def get_all_transaction(address, signature = "", type = transaction_type.values()):
    last_signature = "PToU9AtpEJiduqZXEPjGqP9LWkinCkwokEusBppz7ZUPjHU2rbKuo2QW7wfzkh8Js2agAv25buSz3qS1ussQxdp"
    transactions = []
    for j in range(3):
        try:
            parsed_transaction = TransactionsAPI.get_parsed_transaction_history(address=address, before=last_signature, type=type)
            size = len(parsed_transaction)
            last_signature = parsed_transaction[size-1]["signature"]
            transactions.extend(parsed_transaction)
            print("Now, last signature is:", last_signature)
        except Exception as e:
            message = str(e)
            if (__ERROR_MESSAGE in message):
                index = message.find(__ERROR_MESSAGE)
                start = index + len(__ERROR_MESSAGE)
                end = message.rfind(".")
                last_signature = message[start:end]
                print("Not find, try next signature:", last_signature)
            else:
                print("unkown error, try skip:" + message)

    write_to_file(f"output/json/history/{address}.json", json.dumps(transactions))

    # with open(f"output/json/history/{address}", "w") as fp:
    #     fp.write(json.dumps(transactions))



'''
ValueError: Error: 404: b'{"error":"Failed to find events within the search period. To continue search, query the API again with the `before` parameter set to 3bY9p8QziPTksVKAcxsrd2bAJZrGrGxqsitMqon6hhG3f4gAkmE3EAvCamjw77brdcWZAjcgUWD7UJhJKEEMakUG."}'
'''
__ERROR_MESSAGE = "To continue search, query the API again with the `before` parameter set to "


from helius import TransactionsAPI
from sdk.helius.Context import TransactionsAPI

def transaction_test():
    transactions = ["5CViKrjwHGhYwXFy2K4ZKBW3hBeXLS9o2DAB9yRCpfghteJNyzCGhcqmnrPNNFshXqhaBqieCbGKk5LTN8ZwGDBZ"]
    raw_transactions = TransactionsAPI.get_parsed_transactions(transactions = transactions )
    print(raw_transactions)

def transaction_history_test():
    parsed_transaction_history = TransactionsAPI.get_parsed_transaction_history(address="B5putHnmne6Xs7evGSCdu4NBVLD9gbViZeeYJS1cveUK")
    print(parsed_transaction_history)

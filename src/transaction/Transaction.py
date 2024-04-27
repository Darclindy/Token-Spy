import transaction.enums as enums
from transaction.tools import *
from transaction.enums import *

class TransactionModel:
    def __init__(self, account, price, count, action, timestamp, fee = 0, description = "", signature = "", mint = ""):
        self.account = account
        self.price = price
        self.count = count
        self.action = action
        self.timestamp = timestamp
        self.value = price  * count
        self.fee = fee
        self.signature = signature
        self.description = description
        self.mint = mint

    @staticmethod
    def parse_transfers(origin_transactions, account) -> 'list':
        result = []
        for transactions in origin_transactions:
            result.extend(TransactionModel.parse_transfer(transactions, account))
        return result


    @staticmethod
    def parse_transfer(origin_transaction, account) -> 'list':
        result = []
        account_data = origin_transaction["accountData"]
        native_account = TransactionModel.__filter_by_native_account(
            account_data, account
        )
        spl_account = TransactionModel.__filter_by_spl_token_account(
            account_data, account
        )
        
        solana_transfer = TransactionModel.__parse_solana_transfers(
            native_account,
            lambda count, action: TransactionModel(account ,0, count, action, origin_transaction["timestamp"], description=origin_transaction["description"], fee=origin_transaction["fee"], signature=origin_transaction["signature"], mint = "SOLANA")
        )
        spl_transfer = TransactionModel.__parse_spl_token_transfers(
            spl_account, 
            lambda count, action, mint : TransactionModel(account, 0, count, action, origin_transaction["timestamp"], description=origin_transaction["description"], fee=origin_transaction["fee"], signature=origin_transaction["signature"], mint = mint)
        )

        result.extend(solana_transfer)
        result.extend(spl_transfer)

        return result
    
    def to_dict(self):
        return {
            "price": self.price,
            "count": self.count,
            "action": self.action.name,
            "timestamp": self.timestamp,
            "fee": self.fee,
            "mint": self.mint,
            "signature": self.signature,
            "description": self.description
        }

    
    @staticmethod
    def __filter_by_native_account(data, account):
        result = []
        for item in data:
            if item['account'] == account:
                result.append(item)
        return result
    

    @staticmethod
    def __filter_by_spl_token_account(data, account):
        result = []
        for item in data:
            for token_change in item.get('tokenBalanceChanges', []):
                if token_change['userAccount'] == account:
                    result.append(item)
                    break
        return result

    @staticmethod
    def __parse_solana_transfers(origin_data, generate_model_func) -> 'list':
        result = []
        for item in origin_data:
            count = item["nativeBalanceChange"]
            action = Action.TRANSFER_IN if (count > 0)  else Action.TRANSFER_OUT
            result.append(generate_model_func(count, action))
        return result

    @staticmethod
    def __parse_spl_token_transfers(origin_data, generate_model_func) -> dict:
        result = []
        for item in origin_data:
            for token_balance_change in item["tokenBalanceChanges"]:
                raw_token_amount = token_balance_change["rawTokenAmount"]
                token_amount = raw_token_amount["tokenAmount"]
                decimals = raw_token_amount["decimals"]
                amount = get_actual_amount(token_amount, decimals)

                result.append(generate_model_func(
                    amount,
                    Action.TRANSFER_IN if (amount > 0) else Action.TRANSFER_OUT,
                    token_balance_change["mint"]
                ))
            
        return result

    



    

        

    



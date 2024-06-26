import transaction.enums as enums
from transaction.tools import *
from transaction.enums import *
from utils.date import convert_timestamp_to_utc, round_down_timestamp_to_nearest_five_minutes
from sdk.helius.Metadata import get_token_symbol, get_token_name
from sdk.cmc.crypto_currency.HistoryCurrencyPresenter import fetch_price
from utils.metadata.SymbolCache import SYMBOL_CACHE
from utils.metadata.Format import remove_non_english_chars
import price.PriceCache as price_cache


class TransactionModel:
    def __init__(self, account, price, count, action, timestamp, fee = 0, description = "", signature = "", mint = ""):
        self.account = account
        self.price = 1
        self.count = count
        self.action = action
        self.timestamp = timestamp
        self.utc_timestamp = convert_timestamp_to_utc(round_down_timestamp_to_nearest_five_minutes(timestamp))
        self.value = price  * count
        self.fee = fee
        self.signature = signature
        self.description = description
        self.mint = mint
        self.symbol = "UNKOWN"

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
            lambda count: TransactionModel(account ,0, count, origin_transaction['type'], origin_transaction["timestamp"], description=origin_transaction["description"], fee=origin_transaction["fee"], signature=origin_transaction["signature"], mint = "SOLANA")
        )
        spl_transfer = TransactionModel.__parse_spl_token_transfers(
            spl_account, 
            lambda count, mint : TransactionModel(account, 0, count, origin_transaction['type'], origin_transaction["timestamp"], description=origin_transaction["description"], fee=origin_transaction["fee"], signature=origin_transaction["signature"], mint = mint)
        )

        result.extend(solana_transfer)
        result.extend(spl_transfer)

        return result
    
    def init_metadata(self):
        self.__fetch_token_name()
        self.__fetch_token_price()

    def __fetch_token_name(self):
        if (SYMBOL_CACHE.contains(self.mint)):
            self.symbol = SYMBOL_CACHE.get(self.mint)
        else:
            symbol_respose = get_token_symbol(self.mint)
            self.symbol = remove_non_english_chars(symbol_respose)
            SYMBOL_CACHE.add_symbol(self.mint, self.symbol)
            print("symbol =", self.symbol)


    def __fetch_token_price(self):
        self.price = price_cache.get_price(self.symbol, self.utc_timestamp)
        print(f"fetch token price: {self.symbol} -> {self.price}")


    
    def to_dict(self):
        return {
            "price": f"{self.price:.8f}",
            "count": f"{self.count:.8f}",
            "action": self.action,
            "timestamp": self.utc_timestamp,
            "fee": self.fee,
            "mint": self.mint,
            "signature": self.signature,
            "description": self.description
        }

    
    @staticmethod
    def __filter_by_native_account(data, account):
        result = []
        for item in data:
            if (item['account'] == account and item['nativeBalanceChange'] != 0):
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
            count = item["nativeBalanceChange"] / (10 ** 9)
            model = generate_model_func(count)
            model.init_metadata()
            result.append(model)
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
                model: TransactionModel = generate_model_func(
                    amount,
                    token_balance_change["mint"]
                )
                model.init_metadata()
                result.append(model)
        return result

    



    

        

    



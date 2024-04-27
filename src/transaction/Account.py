from transaction.enums import Chain
from transaction.Token import Token
from transaction.Transaction import TransactionModel
from utils.out import write_to_file
# from utils.excel.ExcelExporter import ExcelExporter
import json

class Account:
    def __init__(self, address) -> None:
        self.chain = Chain.SOL.name
        self.address = address
        self.transaction_dict = dict()

    def get_token(self, mint_address):
        if mint_address not in self.transaction_dict:
            token = Token(mint_address, self.address)
            self.transaction_dict[mint_address] = token
        return self.transaction_dict[mint_address]


    def add_model(self, model: TransactionModel):
        mint = model.mint
        token = self.get_token(mint)
        token.add_model(model)
        

    def add_model_list(self, list):
        for item in list:
            self.add_model(item)
        

    def set_token(self, token: Token):
        self.transaction_dict[token.mint] = token

    def to_dict(self):
        return {
            "address": self.address,
            "token": {
                k: v.to_dict() for k, v in self.transaction_dict.items()
            }
        }

    def write_to_json(self):
        write_to_file(f"json/account/{self.address}.json", json.dumps(self.to_dict()))
        print(f"{self.address} dump finshed.")

    # def write_to_excel(self):
    #     ExcelExporter.export_account(self)
        # data = self.to_dict()

        # # 提取数据并转换为三维列表
        # data_3d = []
        # for token, token_data in data['token'].items():
        #     for model in token_data['models']:
        #         data_3d.append([
        #             [model['price']],
        #             [model['count']],
        #             [model['action']],
        #             [model['timestamp']]
        #         ])

        # print(data_3d)
        
        # exporter = ExcelExporter(filename = f"output/excel/{self.address}.xlsx")
        # exporter.export_3d(data_3d)
        


    

    
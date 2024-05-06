import pandas as pd
from transaction.Account import Account
from sdk.helius.Metadata import get_token_symbols
from utils.out import write_to_file
import json
import os

class ExcelExporter:

    @staticmethod
    def export_account(account: Account):
        data = account.to_dict()
        # 从输入的json数据中提取需要的信息
        data_dict = {}
        for token, token_data in data['token'].items():
            for model in token_data['models']:
                if token not in data_dict:
                    data_dict[token] = []
                data_dict[token].append(model['price'])
                data_dict[token].append(model['count'])
                data_dict[token].append(model['action'])
                data_dict[token].append(f"{model['action']} {float(model['price']) * float(model['count'])}")
                data_dict[token].append(model['timestamp'])

        write_to_file("test.json" ,json.dumps(data_dict))

        column = data_dict.keys()

        # 创建一个空的dataframe
        df = pd.DataFrame(columns=column).astype('object')

        tmp_list = list(column)
        sol_index = tmp_list.index("SOLANA")
        tmp_list.remove("SOLANA")

        symbols = get_token_symbols(tmp_list)

        if (sol_index >= 0):
            symbols.insert(sol_index, "SOLANA")


        df.loc[len(df)] = symbols

        for mint, values in data_dict.items():
            for index in range(len(values)):
                df.loc[index + 1, mint] = str(values[index])

        final_path = f'output/excel/{account.address}.xlsx'
        # 获取文件所在的目录
        directory = os.path.dirname(final_path)

        # 如果目录不存在，则创建它
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 保存为.xlsx文件
        df.to_excel(final_path)




# 使用示例
if __name__ == "__main__":
    # 创建一个示例DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    
    # 创建ExcelExporter对象并导出数据
    exporter = ExcelExporter(dataframe=df)
    exporter.export()

    # 创建一个示例三维列表
    data_3d = [[[i + j + k for k in range(5)] for j in range(5)] for i in range(5)]
    
    # 导出三维列表
    exporter_3d = ExcelExporter(filename='output_3d.xlsx')
    exporter_3d.export_3d(data_3d)
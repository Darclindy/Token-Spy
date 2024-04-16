import pandas as pd

class ExcelExporter:
    def __init__(self, dataframe, filename='output.xlsx'):
        """
        初始化ExcelExporter对象。

        参数:
            dataframe (pandas.DataFrame): 要导出的数据帧。
            filename (str): 输出文件的名称，默认为'output.xlsx'。
        """
        self.dataframe = dataframe
        self.filename = filename

    def export(self):
        """
        将数据帧导出到Excel文件。
        """
        try:
            # 使用to_excel方法将DataFrame写入Excel文件
            self.dataframe.to_excel(self.filename, index=False)
            print(f"Data exported successfully to {self.filename}")
        except Exception as e:
            print(f"Failed to export data: {e}")

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

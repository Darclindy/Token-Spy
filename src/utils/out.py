import os

BASE_PATH = "output/"

def write_to_file(path, text):
    final_path = BASE_PATH + path
    # 获取文件所在的目录
    directory = os.path.dirname(final_path)

    # 如果目录不存在，则创建它
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 打开并写入文件
    with open(final_path , "w") as file:
        file.write(text)
import os

def write_to_file(path, text):
    # 获取文件所在的目录
    directory = os.path.dirname(path)

    # 如果目录不存在，则创建它
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 打开并写入文件
    with open(path , "w") as file:
        file.write(text)
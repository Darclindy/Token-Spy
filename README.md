# 安装环境

venv 是 Python 的标准库之一，用于创建轻量级的虚拟环境。以下是创建和使用虚拟环境的步骤：

## 安装 Python

确保你的系统中安装了 Python。你可以从 Python 官网下载并安装。项目使用的 python 版本号为：

```bash
$ python --version
Python 3.10.12
(.venv)

pip 22.0.2 from /home/clindy/py-program/Token-Spy/.venv/lib/python3.10/site-packages/pip (python 3.10)
(.venv)
```

## 创建虚拟环境

打开命令行工具，然后运行以下命令在仓库目录下创建虚拟环境：

```bash
# path/to/python3.10是指定的 python 解释器的路径
# 如果希望使用完全相同的环境，可以这样保证环境一致
path/to/python3.10 -m venv .venv

# 如果无所谓环境，可以直接使用
python -m venv .venv
```

激活虚拟环境
激活虚拟环境的方法取决于你的操作系统：

Windows:

```bash
.\myenv\Scripts\activate
```

macOS/Linux:

```bash
source myenv/bin/activate
```

安装必要的 Python 包
项目配置在`setup.py`中，运行如下命令配置环境：

```bash
pip install -e .
```

## 配置 API Token

项目数据通过 Dune，CMC，Helius 等平台获取，需要使用平台的 Token。对于一般的项目，平台提供的免费使用次数已经足够，再使用该项目前，建议先从平台获取对应的 Token，将 Token 填入`.env.example`中，再将`.env.example`改名为`.env`。

> API 链接：
>
> - Dune:
> - CMC:
> - Helius: https://github.com/vmpyre/helius_sdk

## 运行实例

```bash
$ token-spy-test #测试项目是否安装
$ test-dune # 测试 dune API
$ test-cmc # 测试 CMC API
$ test-helius # 测试 helius API


(.venv)
```

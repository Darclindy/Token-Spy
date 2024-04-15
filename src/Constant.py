from dotenv import load_dotenv
import os

# 加载.env文件
load_dotenv()

CMC_URL = "https://pro-api.coinmarketcap.com"
CMC_API_KEY = os.getenv("CMC_API_KEY")
DUNE_API_KEY = os.getenv("DUNE_API_KEY")
HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

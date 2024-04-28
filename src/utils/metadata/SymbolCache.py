# mint_address -> symbol



class SymbolCache:
    def __init__(self) -> None:
        self.symbol_cache = dict()
        self.symbol_cache["SOLANA"] = "SOL"

    def add_symbol(self, mint, symbol):
        self.symbol_cache[mint] = symbol
    
    def contains(self, mint):
        return mint in self.symbol_cache.keys()
    
    def get(self, mint):
        if (mint in self.symbol_cache.keys()):
            return self.symbol_cache[mint]
        else:
            return "ERROR2"
    



SYMBOL_CACHE = SymbolCache()

class Token:
    def __init__(self, mint, account):
        self.mint = mint
        self.account = account
        self.balance_now = 1.0
        self.models = []

    def add_model(self, model):
        self.models.append(model)

    def to_dict(self):
        return {
            "mint": self.mint,
            "account": self.account,
            "balance_now": self.balance_now,
            "models": [
                m.to_dict() for m in self.models
            ]

        }


    
    
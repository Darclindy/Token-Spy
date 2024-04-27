from enum import Enum

class Action(Enum):
    UNKOWN = 0
    BUY = 1
    SELL = 2
    TRANSFER_IN = 3
    TRANSFER_OUT = 4

    def to_dict(self):
        return {
            "action": self.value
        }


class Chain(Enum):
    SOL = 0
    ETH = 1
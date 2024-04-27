from transaction import *


def get_actual_amount(token_amount, decimals):
    return int(token_amount) / (10 ** decimals)

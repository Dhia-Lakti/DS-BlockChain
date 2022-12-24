from brownie import firstMe
from scripts.helpful_scripts import get_account


def first():
    first_me = firstMe[-1]
    account = get_account()
    entrance_fee = first_me.getEntranceFee() + 50
    print(entrance_fee)
    print(f"the current fee is {entrance_fee}")
    print("firsting ...")
    first_me.first({"from": account, "value": entrance_fee})


def withdrow():
    first_me = firstMe[-1]
    account = get_account()
    first_me.withdrow({"from": account})


def main():
    first()
    withdrow()

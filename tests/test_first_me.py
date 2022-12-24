from scripts.first_and_withdrow import first
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    FORKED_LOCAL_ENVIRONMENTS,
)
from scripts.deploy import deploy_first_me
from brownie import network, accounts, exceptions
import pytest


def test_can_first_and_withdrow():
    account = get_account()
    first_me = deploy_first_me()
    entrance_fee = first_me.getEntranceFee() + 100
    tx = first_me.first({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert first_me.addressToAmountfirsted(account.address) == entrance_fee
    tx2 = first_me.withdrow({"from": account})
    tx2.wait(1)
    assert first_me.addressToAmountfirsted(account.address) == 0


def test_only_owner_can_withdrow():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local network testing")
    first_me = deploy_first_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        first_me.withdrow({"from": bad_actor})

from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    # local ganache
    # account = accounts[0]
    # print(account)

    # brownie accounts (recommended)
    # account = accounts.load("solidity-tutorial")
    # print(account)

    # env with os
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(acount)

    # env with config
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    account = get_account()

    # contract object
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("solidity-tutorial")


def main():
    deploy_simple_storage()

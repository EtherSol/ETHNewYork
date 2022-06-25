from brownie import accounts, config, MetroToken

initial_supply = 100000000000000000000
token_name = "Metro Token"
token_symbol = "MTNY"

def main():
    account = accounts[0]
    erc20 = MetroToken.deploy(
        initial_supply, {"from":account}
    )
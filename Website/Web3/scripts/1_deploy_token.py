from brownie import accounts, config, TokenERC20

initial_supply = 100000000000000000000
token_name = "Metro Token"
token_symbol = "MTNY"

def main():
    account = accounts[0]
    erc20 = TokenERC20.deploy(
        initial_supply,token_name,token_symbol,{"from":account}
    )
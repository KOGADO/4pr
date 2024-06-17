from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, address_contract

w3= Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))    
w3.middleware_onion.inject(geth_poa_middleware,layer=0)

contract = w3.eth.contract(address=address_contract, abi=abi)

print(f"Баланс пользователя 1: {w3.eth.get_balance('0x2013f636aC331618A8bcd5CfBD23637D5EC7d15A')}")
print(f"Баланс пользователя 2: {w3.eth.get_balance('0x58a7a37fd21bd6b35cA95eeF6148efe6FD1b7352')}")
print(f"Баланс пользователя 3: {w3.eth.get_balance('0x3CFeaB84b97539a656F3C0c1b056B35896C72a6c')}")
print(f"Баланс пользователя 4: {w3.eth.get_balance('0xf973DeE15922C6E22E4fDA2BC50CB4e687d5f36A')}")
print(f"Баланс пользователя 5: {w3.eth.get_balance('0xda08117960603651B84a194790098d250844a3cF')}")



import json
from web3 import Web3, HTTPProvider

url= 'https://sandbox.truffleteams.com/8f7572d1-e253-420a-93bc-2ed8a6f051e6'
w3 = Web3(HTTPProvider(url))
w3.eth.default_account = w3.eth.accounts[0]

with open('abi.json') as f:
    abi = json.load(f)

with open('bytecode.json') as f:
    bytecode = json.load(f)['object']

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Greeter.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
address = tx_receipt.contractAddress

with open('address.txt', 'w') as f:
    f.write(address)
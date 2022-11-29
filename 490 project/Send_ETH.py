#sending funsction from eth wallet
#runs on server that half works & half dont know why it doesnt work

from web3 import Web3, HTTPProvider, IPCProvider
from ethereum.transactions import Transaction
web3 = Web3(HTTPProvider('https://api.myetherapi.com/eth'))


amountExample = Web3.toWie(0.001, 'ether')
tx = Transaction(0, 60000000000, 21000, targetwallet, amountexample, "").sign('yourprivatekey')
print(tx.to_dict())
raw_tx = rlp.encode(tx)
raw_tx_hex = web3.toHex(raw_tx)
web3.eth.sendRawTransaction(raw_tx_hex)

#get balance from your wallet 
#eth.get_balance('usd')   #how much they have in usd
#eth.get_balance('eth')   #how much they have in eth


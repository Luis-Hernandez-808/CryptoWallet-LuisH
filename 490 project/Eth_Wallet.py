# creating an eth wallet using python


from ethereum import utils
from eth_utils import address
import os

private_key = utils.sha3(os.urandom(4096))#this can be changed to the bip320
raw_address = utils.privtoaddr(private_key)#this makes a rando, adress 
addressif = address.to_normalized_address(raw_address)#this makes it look into a regular looking and working wallet
keyether = utils.encode_hex(private_key)# makes private key for eth wallet

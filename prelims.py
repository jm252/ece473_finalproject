from web3 import Web3
from typing import List

# connect to web3
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/0871f5a800a84769844a6657a2eae521'))
# check connection 
res = w3.is_connected()
print(res)

balance = w3.eth.get_balance('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f')
print(balance)
proof = w3.eth.get_proof('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f', [])
print(proof)

# Query by address 
def query_blockchain_by_address(address: str) -> dict:
    # get transactions for the address
    transactions = w3.eth.get_transactions(address)

    return transactions

# Identify MEV bots given a list of addressess
def identify_mev_bot_addresses(addresses: List[str]) -> List[str]:
    mev_bot_addresses = []
    for address in addresses:
        if is_mev_bot(address):
            mev_bot_addresses.append(address)
    return mev_bot_addresses

# Function to check whether MEV bot 
def is_mev_bot(address: str) -> bool:
    # add logic here
    return False # this


# TESt Change


# Find addressess....that what??? 
def explore_blockchain(addresses: List[str]) -> dict:
    blockchain_data = {}
    for address in addresses:
        blockchain_data[address] = query_blockchain_by_address(address)
    return blockchain_data

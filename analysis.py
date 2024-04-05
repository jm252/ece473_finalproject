import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI()

def smart_contract_class(smart_contract):
   response = client.chat.completions.create(
   model="gpt-4",
   messages=[
    {"role": "system", "content": "You are a smart contract assistant. You read a smart contracts and classify it into 1 of 10 categories"},
    {"role": "user", "content": "Classify this smart contract into one of the following 10 categories. Here are the 10 categories, comma seperated. MEV Bot Contracts, DeFi Protocol Contracts, NFT Contracts, Gaming Contracts, DAO Contracts, DEX Contracts, Oracle Contracts, Governance Contracts, Stablecoin Contracts, Tokenization Contracts. Your answer should be just a single category from the sentence prior -- no extra words. Here is the contract to classify: " + smart_contract},
   ])
   return response.choices[0].message.content

# def smart_contract_class(smart_contract):
#   print('hello')
#   prompt = """Please categorize the smart contract into one of the following 10 categories and subcategories. 
#   Respond in the format 'Category, Subcategory':
#     1. MEV Bot Strategies:
#        - Flashbots Arbitrage
#        - Sandwich Attacks
#        - Miner Bribery
#        - Transaction Ordering Strategies
#        - Front-Running

#     2. DeFi Protocols:
#        - Decentralized Lending
#        - Decentralized Exchanges (DEX)
#        - Automated Market Makers (AMM)
#        - Yield Farming Strategies
#        - Liquidity Provisioning Pools

#     3. NFT Platforms:
#        - Art NFT Marketplaces
#        - Gaming NFT Platforms
#        - Collectibles and Trading Cards
#        - Virtual Real Estate Platforms
#        - Domain Name NFT Platforms

#     4. Gaming Contracts:
#        - In-Game Currency Contracts
#        - Item Ownership Contracts
#        - Game Logic and Mechanics
#        - NFT Integration in Games
#        - Gaming Platform Governance

#     5. DAO Contracts:
#        - Voting Mechanisms
#        - Proposal Submission and Management
#        - Treasury Management
#        - Member Onboarding and Offboarding
#        - Governance Token Distribution

#     6. DEX Contracts:
#        - Uniswap V2/V3 Contracts
#        - SushiSwap Contracts
#        - Balancer Pools
#        - Curve Finance Pools
#        - Bancor Contracts

#     7. Oracle Contracts:
#        - Price Feed Oracles
#        - Decentralized Data Oracles
#        - Time-Based Oracles
#        - Reputation-Based Oracles
#        - Custom Data Feeds

#     8. Governance Contracts:
#        - DAO Governance Contracts
#        - Protocol Upgrade Voting Contracts
#        - On-Chain Governance Mechanisms
#        - Token Holder Proposals
#        - DAO Treasury Management

#     9. Stablecoin Contracts:
#        - Collateralized Stablecoins
#        - Algorithmic Stablecoins
#        - Fiat-Collateralized Stablecoins
#        - Crypto-Collateralized Stablecoins
#        - Stablecoin Stabilization Mechanisms

#     10. Tokenization Contracts:
#         - ERC-20 Token Contracts
#         - ERC-721 Token Contracts
#         - ERC-1155 Token Contracts
#         - Security Token Offerings (STOs)
#         - Utility Token Contracts
    
#     Here is the smart contract:

#     """
#   response = model.generate_content(prompt + smart_contract)
#   return response.text

# def smart_contract_read(smart_contract):
#   response = model.generate_content('Please list all of the read only functions. On line 1, provide the function signature. On the next line, describe its input and output as well as purpose in 1-2 sentences.' + smart_contract)
#   return response.text

# def smart_contract_write(smart_contract): 
#   response = model.generate_content('Please list all of the write only functions. On line 1, provide the function signature. On the next line, describe its input and output as well as purpose in 1-2 sentences.' + smart_contract)
#   return response.text

if __name__ == "__main__":
    addy = "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"  

    contract_class = smart_contract_class(addy)

    print(contract_class)
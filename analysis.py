import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyDUks0Swg2DSqKN_gdw6ACl4163NUQuFrc')
model = genai.GenerativeModel('gemini-pro')

def smart_contract_summary(smart_contract):
  response = model.generate_content('Please summarize the function of this smart contract in about 70 words: ' + smart_contract)
  return response.text

def smart_contract_class(smart_contract):
  prompt = """Please categorize the smart contract into one of the following 10 categories and subcategories. 
  Respond in the format 'Category, Subcategory':
    1. MEV Bot Strategies:
       - Flashbots Arbitrage
       - Sandwich Attacks
       - Miner Bribery
       - Transaction Ordering Strategies
       - Front-Running

    2. DeFi Protocols:
       - Decentralized Lending
       - Decentralized Exchanges (DEX)
       - Automated Market Makers (AMM)
       - Yield Farming Strategies
       - Liquidity Provisioning Pools

    3. NFT Platforms:
       - Art NFT Marketplaces
       - Gaming NFT Platforms
       - Collectibles and Trading Cards
       - Virtual Real Estate Platforms
       - Domain Name NFT Platforms

    4. Gaming Contracts:
       - In-Game Currency Contracts
       - Item Ownership Contracts
       - Game Logic and Mechanics
       - NFT Integration in Games
       - Gaming Platform Governance

    5. DAO Contracts:
       - Voting Mechanisms
       - Proposal Submission and Management
       - Treasury Management
       - Member Onboarding and Offboarding
       - Governance Token Distribution

    6. DEX Contracts:
       - Uniswap V2/V3 Contracts
       - SushiSwap Contracts
       - Balancer Pools
       - Curve Finance Pools
       - Bancor Contracts

    7. Oracle Contracts:
       - Price Feed Oracles
       - Decentralized Data Oracles
       - Time-Based Oracles
       - Reputation-Based Oracles
       - Custom Data Feeds

    8. Governance Contracts:
       - DAO Governance Contracts
       - Protocol Upgrade Voting Contracts
       - On-Chain Governance Mechanisms
       - Token Holder Proposals
       - DAO Treasury Management

    9. Stablecoin Contracts:
       - Collateralized Stablecoins
       - Algorithmic Stablecoins
       - Fiat-Collateralized Stablecoins
       - Crypto-Collateralized Stablecoins
       - Stablecoin Stabilization Mechanisms

    10. Tokenization Contracts:
        - ERC-20 Token Contracts
        - ERC-721 Token Contracts
        - ERC-1155 Token Contracts
        - Security Token Offerings (STOs)
        - Utility Token Contracts
    
    Here is the smart contract:

    """
  response = model.generate_content(prompt + smart_contract)
  return response.text

def smart_contract_read(smart_contract):
  response = model.generate_content('Please list all of the read only functions. On line 1, provide the function signature. On the next line, describe its input and output as well as purpose in 1-2 sentences.' + smart_contract)
  return response.text

def smart_contract_write(smart_contract): 
  response = model.generate_content('Please list all of the write only functions. On line 1, provide the function signature. On the next line, describe its input and output as well as purpose in 1-2 sentences.' + smart_contract)
  return response.text
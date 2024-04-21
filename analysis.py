import os
from openai import OpenAI
import google.generativeai as genai
from dotenv import load_dotenv

# ----------------------------------------------------------------------

load_dotenv()
genai_api_key = os.getenv("GENAI_API_KEY")

# set up openai
os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI()

# set up genai
genai.configure(api_key=genai_api_key)
model = genai.GenerativeModel('gemini-pro')

# ----------------------------------------------------------------------

# classify smart contract given code
def smart_contract_class(smart_contract):
   response = client.chat.completions.create(
   model="gpt-4",
   messages=[
    {"role": "system", "content": "You are a smart contract assistant. You read a smart contracts and classify it into 1 of 10 categories"},
    {"role": "user", "content": "Classify this smart contract into one of the following 10 categories. Here are the 10 categories, comma seperated. MEV Bot Contracts, DeFi Protocol Contracts, NFT Contracts, Gaming Contracts, DAO Contracts, DEX Contracts, Oracle Contracts, Governance Contracts, Stablecoin Contracts, Tokenization Contracts. Your answer should be just a single category from the sentence prior -- no extra words. Here is the contract to classify: " + smart_contract},
   ])
   return response.choices[0].message.content

# summarize smart contract given code 
def smart_contract_summary(smart_contract):
  response = model.generate_content('Please summarize the function of this smart contract in about 70 words: ' + smart_contract)
  return response.text

# return smart contract read functions given code
def smart_contract_read(smart_contract):
   response = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[
    {"role": "system", "content": "You are a smart contract assistant. You read a smart contracts and identify which functions are read and which are write "},
    {"role": "user", "content": "Please list all of the read only functions. On line 1, provide the function signature. On the next line, describe its input and output as well as purpose in 1-2 sentences. Here is the contract: " + smart_contract},
   ])
   return response.choices[0].message.content

# return smart contract write functions given code 
def smart_contract_write(smart_contract): 
   response = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[
      {"role": "system", "content": "You are a smart contract assistant. You read a smart contracts and identify which functions are read and which are write "},
      {"role": "user", "content": "Please list all of the write only functions. On line 1, provide the function signature. On the next line, describe its input and output as well as purpose in 1-2 sentences. Here is the contract: " + smart_contract},
   ])
   return response.choices[0].message.content

import os
from openai import OpenAI
import google.generativeai as genai
from dotenv import load_dotenv

# ----------------------------------------------------------------------

load_dotenv()
genai_api_key = os.getenv("GENAI_API_KEY")

# set up openai
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
def summarize_read_functions(read_functions, smart_contract):
   response = client.chat.completions.create(
   model="gpt-4-turbo",
   messages=[
    {"role": "system", "content": "You are a smart contract assistant. You read a smart contract and a list of function signatures and summarize each function based on it's corresponding code."},
    {"role": "user", "content": read_function_prompt + ''.join(str(func) for func in read_functions)},
    {"role": "assistant", "content": "Here is the smart contract to base your answer off of: " + smart_contract},
   ])
   return response.choices[0].message.content

# return smart contract write functions given code 
def summarize_write_functions(write_functions, smart_contract): 
   response = client.chat.completions.create(
   model="gpt-4-turbo",
   messages=[
       {"role": "user", "content": write_function_prompt + ''.join(str(func) for func in write_functions)},
      {"role": "assistant", "content": "Here is the smart contract to base your answer off of: " + smart_contract},
   ])
   return response.choices[0].message.content


read_function_prompt = """ 
Please list all of the read only functions provided in this list and a summary for each one. On line 1, provide the function signature. On the next line, describe the function purpose in 1-2 sentences according to the contract provided to you. Do not add extra characters, just use newline spaces and ensure consistent formatting throughout. Here is an example: 
name() returns (string)
This function provides the name of the token.

And here are the read only functions:
"""
write_function_prompt = """
Please list all of the write only functions provided in this list and a summary for each one. On line 1, provide the function signature. On the next line, describe the function purpose in 1-2 sentences according to the contract provided to you. Do not add extra characters, just use newline spaces and ensure consistent formatting throughout. Here is an example: 
name() returns (string)
This function provides the name of the token.

And here are the write only functions:
"""


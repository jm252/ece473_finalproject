import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyDUks0Swg2DSqKN_gdw6ACl4163NUQuFrc')
model = genai.GenerativeModel('gemini-pro')

def smart_contract_summary(smart_contract):
  response = model.generate_content('Please explain the function of this smart contract: ' + smart_contract)
  return response.text
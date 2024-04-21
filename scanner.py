import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
API_KEY = os.getenv("ETHERSCAN_API_KEY")

def get_contract_code(addy) -> str:
    """
    Retrieve smart contract code associated with an Ethereum address using the Etherscan API.
    
    Parameters:
    - address (str): The Ethereum address for which to retrieve the smart contract code.

    Returns:
    - str: The smart contract code.
    """

    # verify that address is contract ????

    url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={addy}&apikey={API_KEY}"

    try:
        response = requests.get(url)
        response_json = response.json()

        if response.status_code == 200 and response_json['status'] == '1':
            contract_code = response_json['result'][0]['SourceCode']
            return contract_code
        else:
            print("Error:", response_json['message'])
            return 
        
    except Exception as e:
        print("Error:", str(e))
        return 

def get_contract_functions(addy):

    url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={addy}&apikey={API_KEY}"

    url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={addy}&apikey={API_KEY}"
    
    try:
        response = requests.get(url)
        response_json = response.json()
        if response.status_code == 200 and response_json['status'] == '1':
            abi = json.loads(response_json['result'])
            read_functions = []
            write_functions = []
            for item in abi:
                if item['type'] == 'function':
                    name = item['name']
                    inputs_str = ', '.join([f"{param['type']} {param['name']}" for param in item['inputs']]) or ""
                    outputs_str = ', '.join([f"{param['type']} {param['name']}" for param in item['outputs']]) or ""
                    func_signature = f"{name}({inputs_str})"
                    if outputs_str:
                        func_signature += f" returns ({outputs_str})"
                    
                    print(func_signature)
                    if not item.get('constant', False):
                        write_functions.append(func_signature)
                    else:
                        read_functions.append(func_signature)
            return read_functions, write_functions
        else:
            print("Error:", response_json['message'])
            return None, None
    except Exception as e:
        print("Error:", str(e))
        return None, None

if __name__ == "__main__":
    addy = "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"  

    # contract_code = get_contract_code(addy)
    # print(contract_code)

    read_functions, write_functions = get_contract_functions(addy)
    print("Num read", len(read_functions))
    print("Num write", len(write_functions))



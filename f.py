

from web3 import Web3

def get_balance(address):
    # Connect to an Ethereum node
    w3 = Web3(Web3.HTTPProvider()

    # Check if connected to Ethereum node
    if w3.isConnected():
        # Get the balance of the specified address
        balance_wei = w3.eth.getBalance(address)
        
        # Convert wei to ether
        balance_eth = w3.fromWei(balance_wei, 'ether')

        return balance_eth
    else:
        return None

if __name__ == "__main__":
    ethereum_address = input('Enter Ethereum address >>> ')

    balance = get_balance(ethereum_address)

    if balance is not None:
        print(f'Balance of {ethereum_address}: {balance} ETH')
    else:
        print('Failed to connect to Ethereum node')

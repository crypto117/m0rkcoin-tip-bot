from typing import List, Dict

from rhodiumcoin_tip_bot import rpc_client
from rhodiumcoin_tip_bot.config import config


def register() -> str:
    result = rpc_client.call_method('createAddress')
    return result['address']


def send_transaction(from_address: str, to_address: str, amount: int) -> str:
    payload = {
        'addresses': [from_address],
        'transfers': [{
            "amount": amount,
            "address": to_address
        }],
        'fee': config.tx_fee,
        'anonymity': 0
    }
    result = rpc_client.call_method('sendTransaction', payload=payload)
    return result['transactionHash']


def get_wallet_balance(address: str) -> Dict[str, int]:
    result = rpc_client.call_method('getBalance', {'address': address})
    return result


def get_all_balances(wallet_addresses: List[str]) -> Dict[str, Dict]:
    wallets = {}
    for address in wallet_addresses:
        wallet = rpc_client.call_method('getBalance', {'address': address})
        wallets[address] = wallet
    return wallets

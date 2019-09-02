#!/usr/bin/python
# import bitcoinrpc
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import yaml
import json
from btctools import Transaction


def getblockhash(height):
    """taking in block height and return block hash"""
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    url = cfg['bitcoind']['url']
    rpc_connection = AuthServiceProxy(url)
    blockhash = rpc_connection.getblockhash(height)
    print("blockhash of height " + str(height) + " = " + blockhash )
    print(rpc_connection.getblock(blockhash))
    print(height)
    #print(rpc_connection.getrawtransaction(''))
    rawtransaction = rpc_connection.getrawtransaction('75a98ce35b869772adbf643b3f8acadfa5b46b4cd8bfef26f9e079c517018285')
    print(rawtransaction)
    tx = Transaction.from_hex(rawtransaction)
    print(tx.json().dumps(parsed, indent=4, sort_keys=True))

if __name__ == "__main__":
    getblockhash(300000)

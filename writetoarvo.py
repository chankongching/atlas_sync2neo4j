#!/usr/bin/python
# import bitcoinrpc
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import yaml

def getblockhash(height):
    """taking in block height and return block hash"""
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    url = cfg['bitcoind']['url']
    rpc_connection = AuthServiceProxy(url)
    blockhash = rpc_connection.getblockhash(height)
    print("blockhash of height " + str(height) " = " + blockhash )
    print(rpc_connection.getblock(best_block_hash))
    print(height)

if __name__ == "__main__":
    getblockhash(1)

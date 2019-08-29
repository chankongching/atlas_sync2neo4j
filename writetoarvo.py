#!/usr/bin/python
import bitcoinrpc
import yaml

def getblockhash(height):
    """taking in block height and return block hash"""
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    url = cfg['bitcoind']['url']
    rpc_connection = bitcoinrpc.AuthServiceProxy(url)
    best_block_hash = rpc_connection.getbestblockhash()
    print(rpc_connection.getblock(best_block_hash))
    print(height)

if __name__ == "__main__":
    getblockhash(1)

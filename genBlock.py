import glob
import os
import sys
import hashlib
import time
import pickle

storage = "Blocks"
lastBlock = None

"""
Block ma strukture:

nr:
dane:
timestamp:
hash:
hashpoprzedniego blocku:

"""

def readBlock(filename):
    block = None
    with f as open(filename,"r+"):
        block = pickle.load(f)
    return block

def saveBlock(filename, block):
    with f as open(filename, "w+"):
        pickle.dump(block, f)

def getLastBlock():
    if lastBlock:
        return lastBlock

    #if no last block was in the memory

    listofBlocks = glob.glob("storage/*.block")

    if not listofBlocks:
        return None
    else:
        listofBlocks.sort()
        listofBlocks.reverse()
        return readBlock(listofBlocks[0])

def createABlock(data):
    lastblock = getLastBlock()
    lastBlockHash = 0
    lastNumber = 0
    if lastblock:
        lastBlockHash = lastBlock['hash']
        lastNumber = lastBlock['nr']

    timestamp = time.time()
    hashdane = hashlib.sha256(data)
    number = lastNumber + 1

    newBlock = {
        'nr' : number,
        'data' : data,
        'hash' : hashdane,
        'timestamp' : timestamp,
        'lasthash' : lastBlockHash
    }

    path = storage + str(number) + ".block"


    return newBlock, hashdane, path


if __name__ == "__main__":
    pass
import glob
import os
import sys
import hashlib
import time
import pickle
import getVATstatusSelenium
import getVATstatus
import numpy as np

storage = "Blocks"
class info:
    lastBlock = None
    def __init__(self):
        self.lastBlock = None



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
    with open(filename,"r+") as f:
        block = pickle.load(f)
    return block

def saveBlock(filename, block):
    with open(filename, "w+") as f:
        pickle.dump(block, f)

def getLastBlock():
    if info.lastBlock:
        return info.lastBlock

    #if no last block was in the memory

    listofBlocksStr = glob.glob(storage + "/*.block")

    listofBlocks = map(lambda x : int(x.split("/")[1].split(".")[0]), listofBlocksStr)
    #print listofBlocks
    if not listofBlocks:
        return None
    else:
        listofBlocks.sort()
        listofBlocks.reverse()
        lastBlock = readBlock(storage + "/" + str(listofBlocks[0]) + ".block")
        info.lastBlock = lastBlock
        print lastBlock
        return lastBlock

def createABlock(data):
    lastBlock = getLastBlock()

    lastBlockHash = 0
    lastNumber = 0
    if lastBlock:
        lastBlockHash = lastBlock['hash']
        lastNumber = lastBlock['nr']
        #print lastNumber

    timestamp = time.time()
    hashdane = hashlib.sha256(str(data)).hexdigest()
    number = lastNumber + 1

    newBlock = {
        'nr' : number,
        'data' : data,
        'hash' : hashdane,
        'timestamp' : timestamp,
        'lasthash' : lastBlockHash
    }

    path = storage + "/" + str(number) + ".block"

    #print newBlock
    info.lastBlock = newBlock
    #print path
    saveBlock(path, newBlock)
    return newBlock, hashdane, path

def checksum(nip):
    suma=0
    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    for i in xrange(9):
        suma+=int(nip[i])*weights[i]
    return suma % 11


if __name__ == "__main__":
    nip=raw_input('Enter NIP: ')
    if len(nip)!=10 or int(nip[9])!=checksum(nip):
        print 'NIP is not correct'
    else:
        status = getVATstatusSelenium.getVATstatus(nip)
        newBlock, hashdane, path = createABlock(status)
        print newBlock


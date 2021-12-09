import datetime
import hashlib


class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hashed(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def output(self):
        self.result = {"Block Hash": str(self.hashed()), "BlockNo": str(self.blockNo), "Block Data": str(
            self.data), "Hashes": str(self.nonce), "Time": str(self.timestamp)}
        return self.result
    def __str__(self):
        self.output()
        return "Time: " + str(self.timestamp) +"\nBlock Hash: " + self.result["Block Hash"] + "\nBlockNo: " + self.result["BlockNo"] + "\nBlock Data: " + self.result["Block Data"] + "\nHashes: " + self.result["Hashes"] + "\n--------------"


class Blockchain:
    diff = 19
    maxNonce = 2 ** 32  # max no that can be stored in a 32bit number, its ued to make a guess
    target = 2 ** (256 - diff)  # control the accepted hashes thus takes more time to mine

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hashed()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        print(block)
        self.block = self.block.next

    def mine(self, block):

        for n in range(self.maxNonce):

            if int(block.hashed(), 16) <= self.target:
                self.add(block)

                break
            else:
                block.nonce += 1






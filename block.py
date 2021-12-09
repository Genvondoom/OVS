from HashingSystem import *
from logsystem import *

blockchain = Blockchain()
candidates = ['ade', "tola", "vondoom"]
vote = ['ade', 'vondoom', 'tola', 'vondoom', 'vondoom']

for n in vote:
    blockchain.mine(Block(n))

results = []

while blockchain.head is not None:
    results.append(blockchain.head.output())
    Log().message_log(blockchain.head)
    #blockchain.head = blockchain.head.next





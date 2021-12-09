from scratch_1 import *

dbTest = []


def hashVotes(data):
    """Hashes Votes then appends them to database using the lenght of database entries and benchmark to which data to upload"""
    unHashed.append(data)
    mineer()
    for votes in chain[len(dbTest):]:
        dbTest.append(votes)


for x in range(100):
    hashVotes([f"am a shoe{x}", "president", datetime.datetime.now()])
for x in dbTest:
    print(x)

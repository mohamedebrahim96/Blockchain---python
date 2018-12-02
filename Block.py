import array as arr
class Block:
    def __init__(self,previousHash,transactions):
        self.previousHash = previousHash
        self.transactions = transactions
        contens = [hash(str(transactions)), previousHash]
        self.blockHash = hash(str(contens))

    @property
    def previousHash(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self.previousHash
    def getpreviousHash(self):
        return self.previousHash
    def gettransactions(self):
        return self.transactions
    def getblockHash(self):
            return self.blockHash


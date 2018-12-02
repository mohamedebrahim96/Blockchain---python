from Block import Block



genesisTransactions =["a saoshi sent ivan 999900 bitcoin","hal finney sent 10 bitcoins to ivan"]
genesisBlock = Block(0, genesisTransactions)

block2Transactions = ["ivan sent 10 bitcoin to satoshi", "satoshi sent 10 bitcoin to starbuck"]
block2 = Block(genesisBlock.getblockHash(), block2Transactions)

block3Transactions = ["ivan sent 999 bitcoin to my mo"]
block3 = Block(block2.getblockHash(), block3Transactions)

print("Hash of genesis block::")
print(genesisBlock.getblockHash())

print("Hash of block 2:")
print(block2.getblockHash())

print("Hash of block 3:")
print(block3.getblockHash())

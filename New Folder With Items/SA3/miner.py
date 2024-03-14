from time import time
from blockchain import Block

class Miner():
    def __init__(self, address):
        self.address= address
        self.walletBalance = 0    
   
    def createBlock(self, index, transactions):
        if(len(transactions) >=3 ):
            transactions = transactions[:3]

            if index==0:
                index = 1
            blockData = {
                    'index': index,
                    'timestamp': time(),
                    'previousHash': "No Previous Hash.",
            }    

            currentBlock = Block(
                                blockData["index"], 
                                blockData["timestamp"], 
                                blockData["previousHash"])
             
            currentBlock.transactions = transactions
            return currentBlock
        return False
    
    # Define reward method that takes currentBlock (mined block)
    def reward(self, currentBlock):
        # Formula to calculate the block reward 
        # Block Reward = (Base Reward) + Transaction Fee
        # Set initial value of baseReward to 5 i.e base value
        baseReward = 5
        # Set transaction fee to 0
        transactionFee = 0
        # Lop through each transaction in transactions
        for transaction in currentBlock.transactions:
            # Add transaction['transactionFeeEther'] to transactionFee
            transactionFee += transaction['transactionFeeEther']

        # Add blockReward and tranactionFee to get blockReward 
        blockReward = baseReward + transactionFee
        # Add minerReward to walletBalance
        self.walletBalance+= blockReward
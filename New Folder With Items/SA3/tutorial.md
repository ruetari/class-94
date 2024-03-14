SA3

Update the Reward Balance
==========================


In this activity, you will learn to calculate the block reward for mining the transactions and add it to the miner’s wallet balance.




<img src= "https://s3-whjr-curriculum-uploads.whjr.online/b99f79c2-d1ac-4aa2-81e4-687afe4ac429.gif" width = "480" height = "320">




Follow the given steps to complete this activity:


* Open the file miner.py.


* Define a method to calculate reward for the currentBlock(mined block).


    `def reward(self, currentBlock):`


* Set the initial value of base reward to 5.
       
    `baseReward = 5`
      
* Set transaction fee to 0.
       
    `transactionFee = 0`


* Loop through each transaction in transactions and add their fee.
       
    `for transaction in currentBlock.transactions:`
    
    &emsp;&emsp;`transactionFee += transaction['transactionFeeEther']`


* Calculate block reward as sum of base reward and transaction fee
       
    `blockReward = baseReward + transactionFee`


* Add the block reward to the miner’s walletBalance.
       
    `self.walletBalance += blockReward`


* Save and run the code to check the output.
SA2
Add the Miners
===============


In this activity, you will learn to help the miner mine the first three transactions from the pending transactions list.




<img src= "https://s3-whjr-curriculum-uploads.whjr.online/d4be5e3c-e348-46d1-b015-a2ac82162142.gif" width = "480" height = "320">




Follow the given steps to complete this activity:
* Open the file miner.py.


* Define a method to create a block by taking the index of the block and transactions list.


    `def createBlock(self, index, transactions):`


* Check if the number of transactions is greater than three, then fetch the first 3 transactions for creating a block.


    `if(len(transactions) >=3 ):`
    
    &emsp;&emsp;`transactions = transactions[:3]`


* Create a block by copying the code from commented code in app.py.
           
    `if index==0:`
    
    &emsp;&emsp;`index = 1`
    
    &emsp;&emsp;`blockData = { 'index': index,        'timestamp': time(),'previousHash': "No Previous Hash.",
    }`
    
    &emsp;&emsp;`currentBlock = Block(
                        blockData["index"],
                        blockData["timestamp"],
                        blockData["previousHash"])`


* Store the transactions in the current block and return the current block.


    `currentBlock.transactions = transactions`
    
    `return currentBlock`


* Return false if the number of pending transactions are less than three.
    
     `return False`


* Open the file blockchain.py.


* Define a method for mining pending transactions that takes the miner address to identify the miner.


    `def minePendingTransactions(self, minerAddress):`
* Loop through each miner to find the miner with the address.
   
   `for miner in self.miners:`
   
   &emsp;&emsp;`if miner.address == minerAddress:`


* Let the miner create the current block if the miner address is found.
    `currentBlock = miner.createBlock(len(self.chain), self.pendingTransactions)`
* If the current block is created, validate the block and add it to the blockchain.

    `if(currentBlock):`
    
    &emsp;&emsp;`isBlockAdded = self.addBlock(currentBlock)`
    
    &emsp;&emsp;`if(isBlockAdded): `
    
    &emsp;&emsp;&emsp;&emsp;`isValid = self.validateBlock(currentBlock)`
    
    &emsp;&emsp;&emsp;&emsp;`currentBlock.isValid = isValid`


 * Remove first three transactions from the pending transactions list.
`self.pendingTransactions = self.pendingTransactions[3:]`


* Open the file app.py.


* Call the mine pending transactions method when the user clicks on the Mine Transactions button from the miningPool() function.
 
    `if request.method == "POST":`
    
    &emsp;&emsp;`minerAddress = request.form.get("miner")`
    
    &emsp;&emsp;`chain.minePendingTransactions(minerAddress)` 


* Save and run the code to check the output.
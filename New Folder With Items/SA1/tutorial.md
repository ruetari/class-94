SA1

Add Transactions to the Mining Pool
===================================


In this activity, you will learn to add the transactions in the mining pool and display them on the web page for the miners to pick.



<img src= "https://s3-whjr-curriculum-uploads.whjr.online/b6b5db4d-ad37-453e-adac-c872895899af.gif" width = "480" height = "320">




Follow the given steps to complete this activity:


* Open the file blockchain.py.


* Create a list to store all the pending transactions that are yet to be mined in the init() of Blockchain class.


    `self.pendingTransactions = []`




* Define a function in the Blockchain class to add a new transaction to the mining pool.


    `def addToMiningPool(self, transaction):
     		self.pendingTransactions.append(transaction)`
`


* Open the file app.py.


* Add the new transaction to the mining pool when the buy button is clicked.


    `chain.addToMiningPool(transaction)`
   
* Stop creating blocks with transactions by commenting all the code that is marked.
* Display the pending transactions on the mining pool web page by rendering the pending transactions list in the miningPool() function.
 
    `return render_template('miningPool.html', pendingTransactions = chain.pendingTransactions)`  
* Save and run the code to check the output.
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Bank_Automation:

    def __init__(self, balance):
        self.balance = balance   

    def transfer(self, account1, account2, money):
        if account1>0 and account1 <len(self.balance)+1 and account2>0 and account2 <len(self.balance)+1:
            if self.balance[account1-1] >=money:
                self.balance[account1-1] = self.balance[account1-1] - money
                self.balance[account2-1] = self.balance[account2-1] + money
                transaction = True
            else:
                transaction = False
        else:
            transaction = False
            
        return transaction  
        
    def deposit(self, account, money):
        if account > 0 and account <len(self.balance)+1:
            self.balance[account-1] =  self.balance[account-1] + money
            transaction = True
        else:
            transaction = False
        return transaction

    def withdraw(self, account, money):
        if account > 0 and account <len(self.balance)+1 and self.balance[account-1]>=money:
            self.balance[account-1] =  self.balance[account-1] - money
            transaction = True
        else:
            transaction = False
        return transaction
        


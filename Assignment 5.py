#!/usr/bin/env python
# coding: utf-8

# # Challenge 1: Square Numbers and Return Their Sum

# In[2]:


class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        return self.x**2+self.y**2+self.z**2
p=Point(1,3,5)
print("Sample method output",p.sqSum())


# # Challenge 2: Implement a Calculator Class

# In[4]:


class Calculator:
    def __init__(self,num1=0,num2=0):
        self.num1=0
        self.num2=0
    def __add__(self):
        return self.num1+self.num2
    def __sub__(self):
        return self.num1-self.num2
    def __mul__(self):
        return self.num1*self.num2
    def __floatdiv__(self):
        return self.num1/self.num2
c=Calculator(10,94)
print("Addition is:", 10+94)
print("Subtraction is:", 94-10)
print("Multiplication is:", 10*94)
print("Division is:", 94/10)


# # Challenge 3: Implement the Complete Student Class

# In[6]:


class Student:
    def __init__(self,name=0,rollno=0):
        self.__name=name
        self.__rollno=rollno
        
    def set_name(self,x):
        self.__name=x
        return""
    def set_rollno(self,y):
        self.__rollno=y
        return""
    def get_name(self):
        return self.__name
    def get_rollno(self):
        return self.__rollno
s=Student()
print(s.set_name("Debraj"))
print(s.set_rollno("8"))
print("Your name is:",s.get_name())
print("Your roll no is:",s.get_rollno())


# # Challenge 4: Implement a Banking Account

# In[2]:


class Account:
    def __init__(self,Title=None,balance=0):
        self.Title=Title
        self.balance=balance
        print("Name is:",self.Title)
        print("Balance is:",self.balance)

class SavingsAccount(Account):
    def __init__(self,Title=None,balance=0,interestrate=0):
        super().__init__(Title,balance)
        self.interestrate=interestrate
        print("Interest rate:",self.interestrate)
a=SavingsAccount("Asish",5000,5)


# # Challenge 5: Handling a Bank Account

# In[1]:


import sys
class Account:
    Bank="State Bank of India"
    def __init__(self,Title=None,Balance=0):
        self.Title=Title
        self.Balance=Balance
        print("Welcome to:",Account.Bank +self.Title)
        print("-"*100)
    def deposit(self,deposit):
        self.Balance=self.Balance+deposit
        return self.Balance
    def withdrawal(self,withdrawal):
        self.withdrawal=withdrawal
        if self.Balance<self.withdrawal:
            print("Insufficient Balance you can't withdraw")
            sys.exist()
        else:
            self.Balance=self.Balance-self.withdrawal
            return self.Balance
    def get_Balance(self):
        return self.Balance
class SavingAccount(Account):
    def __init__(self,Title=None,Balance=0,interestrate=0):
        super().__init__(Title,Balance)
        self.interestrate=interestrate

        print("-"*100)
    def InterestAmount(self):
        print("Interest Rate:",self.interestrate)
        return (self.interestrate*self.Balance)//100
a=SavingAccount("Asish",2000,5)
print(a.deposit(500))
print(a.get_Balance())
a.withdrawal(500)

print(a.get_Balance())
print(a.InterestAmount())


# In[ ]:





# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:28:25 2019

@author: sagar
"""
def fibonacci(limit):
    #To find out the fibonacci sequence using loop.
    #Input the number upto which you want to find out the sequence
    #first two numbers of the sequence are assigned 0,1
    fib1,fib2 = 0,1
    #initializing count sequence to keep a count of numbers processed
    count = 0
    #Loop until the limit is encountered
    while (count<limit):
    #if the limit is zero, prompt user to enter a number
        if (limit == 0):
         print("enter a number")
         exit()
    #if the limit is 1 display the first number of the sequence
    	elif (limit == 1):
         exit()
    #Loop until the end and print the sequence at each iteration
    	else:
         count+=1
         print("fibonacci term",count,"is",fib1)
         fib1,fib2 = fib2,fib1+fib2
         
    return (0)
    
if __name__ == "__main__":
    
    limit = int(input("enter limit"))
    print(fibonacci(limit))

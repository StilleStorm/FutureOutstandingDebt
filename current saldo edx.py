# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 20:25:00 2018

@author: StilleStorm
"""

# Python 3
# Program for calculating remaining balance on a credit after 12 months 
# Variables\ inputs needed are balance, annaual interest rate and monthly payment rate

#variables. Do not include in code for grader
balance = 5000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#variables. These are to be included in grader.

#counting monthly interest rate based on annual interest rate.
monthlyInterestRate = annualInterestRate / 12

#months to count. In future (if usefulll outside gdader) could be input
#set to default 12 for grader
m = 12
 

#Defining function for minimal monthly payment for given month.
def monthpayment(pb):
    """counting minimal monthly payment. 
    input should be previus balance (pb) for given month """ 
    
    # Returning rounded value counted for cuurenty month payment
    return monthlyPaymentRate * pb
    print (str(monthlyPaymentRate(pb)))

#Defining main outstanding debtr couting function
def outstandingDebt(m):
    """function calculates outstanding debt for m months in future.
    it counts only minimal payments paid. Rounded to 2 decimal places"""
    
    #Set of variables for iteration
    #count for counting down months, pb for first time previus balance, analogic for current balance
    count = m
    pb = balance
    currbalance = balance
    
    #Iteration for counting  down month by month saldo
    while count > 0:
        #changing current balance by lowering amout by monthly payment for current month
        #and adding monthly interest rates
        print 
        currbalance = round(currbalance - monthpayment(pb), 2)
        currbalance = round(currbalance + currbalance * monthlyInterestRate, 2)
        #changing count and pb (prevoius balance) accordingly
        pb = currbalance
        count -= 1
        # remove hashtag in line below if you want to see month by mont saldo
        #print(currbalance)
    
    #when cont for numbers of months runs down print summary of balance after given period    
    if count == 0:
        saldo = round(currbalance, 2)
        print("Remaining balance: " + str(saldo))

outstandingDebt(m)
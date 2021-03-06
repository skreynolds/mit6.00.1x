#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:01:14 2017

@author: shane

Now write a program that calculates the minimum fixed monthly payment needed
in order pay off a credit card balance within 12 months. By a fixed monthly
payment, we mean a single number which does not change each month, but
instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will
pay off all debt in under 1 year, for example:

Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at
the end of the month (after the payment for that month is made). The
monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become negative using this
payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) +
                             (Monthly interest rate x Monthly unpaid balance)

Test Cases to Test Your Code With. Be sure to test these on your
own machine - and that you get the same output! - before running your code
on this webpage!
Click to See Problem 2 Test Cases

The code you paste into the following box should not specify the values for the variables balance or annualInterestRate - our test code will define those values before testing your submission.
"""

# Test Case
balance = 3329
annualInterestRate = 0.2

"""My code here"""

monthlyInterestRate = annualInterestRate / 12.0;
monthlyUnpaidBalance = balance;
minimumFixedPayment = 10;

while(True):
    
    # Reset balance to original amount
    monthlyUnpaidBalance = balance;
    
    # Determine if the balance will be paid off
    for i in range(1,13):
        monthlyUnpaidBalance -= minimumFixedPayment;
        monthlyUnpaidBalance += monthlyInterestRate*monthlyUnpaidBalance;
    
    if (monthlyUnpaidBalance > 0):
        # Increase the monthly payment by 10
        minimumFixedPayment += 10;
    else:
        break       
print('Lowest Payment: ' + str(minimumFixedPayment));

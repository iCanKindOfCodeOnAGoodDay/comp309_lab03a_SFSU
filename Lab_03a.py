"""
    CSC 309 SFSU Spring 2023
    Lab #3a
    Created on Wed Feb  00:33:07 2024
    Last updated on Wed Feb  02:27:49 2024
    @author: scottquashen
    
    Description: 
        This program implements two functions that check1 if a list is sorted. 
        
    Inputs: 
        List

    Outputs: 
        Print: Labels in console, Return: String representing the result of check

    Dependencies: time

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.2.1
"""

#imports 
import time



#Create three lists
L1=[1, 0, 2, 3, 4]
L2=[0, 1, 2, 4, 3]
L3=[0, 1, 4, 3, 2]

L4 = [0,1,2,3,4]

# Write a function to test if a list is sorted using for loop, return True if list is sorted
# else return False. The function has one argument: a Python List.

def check1(someList):
    """ 

----This function check1s if of numbers are in numerical order.
The loop can end in 2 ways. 1) return failure 2) return success

----Inputs: List of type int

----Output: nothing

----Returns: string result

Usage: check1(L1)

    """    
    for i in range(len(someList)):
        if i > 0:
            if someList[i - 1] > someList[i]:
                return "Non-ascending"
            if i == len(someList) - 1:
                return "Ascending"

def check2(someList):
    
    """ 

----This function check1s if items within a list of numbers are in numerical.
The while loop can end in 2 ways. 1) Return failure 2) Return success

----Inputs: List of type int

----Output: nothing

----Returns: string 

Usage: check2(L1)
    """
    
    i = 0
    while i <= len(someList):
        if i > 0:
            if someList[i - 1] > someList[i]:
                return "Non-ascending"
            if i == len(someList) - 1:
                return "Ascending"
        i += 1
    
    
    


""" FUNCTION CALLS BELOW"""
            
print("Scott Quashen... ", time.asctime())
        
# Invoke the for-loop function 3 times, passing in L1, then L2, then L3, 
# and print the sorted status after each invocation
print('\nFirst we will use a for in loop to check1 if lists are in ascending order.')

check1(L1)
print(check1(L1))

check1(L2)
print(check1(L2))

check1(L3)
print(check1(L3))


# Invoke the while-loop function 3 times, passing in L1, then L2, then L3, 
# and print the sorted status after each invocation
print('\nNow, the while loops will be used to check1.')

check2(L1)
print(check2(L1))

check2(L2)
print(check2(L2))

check2(L3)
print(check2(L3))




# Use the built-in sort() method to sort the list of random numbers.
L1.sort()
print("\nWe just sorted the list, so now lets make sure the functions are working.")

# Call the for-loop function to test sorted status, print results
check1(L1)
print(check1(L1))

# Call the while-loop function to test sorted status, print results
check2(L1)
print(check2(L1))






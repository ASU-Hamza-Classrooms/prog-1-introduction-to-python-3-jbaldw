#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    print("Input string is " + inputStr)
    print("Reverse of string is " + reverseStr(inputStr))
    print("Does string contain apple? " + containsWord(inputStr, "apple"))
    print("Does string contain banana? " + containsWord(inputStr, "apple"))
    print("Is string a palindrome? " + isPalindrome(inputStr))
    print("Uppercase of string is " + upperCaseStr(inputStr))
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    #Add code to create a Worker object
    #Use the object to call each of the methods in the Worker class
    #Print the result of each call
    worker = Worker(inputStr)
    print("Input string is " + inputStr)
    print("Reverse of string is " + worker.reverseStr())
    print("Does string contain apple? " + worker.containsWord("apple"))
    print("Does string contain banana? " + worker.containsWord("apple"))
    print("Is string a palindrome? " + worker.isPalindrome())
    print("Uppercase of string is " + worker.upperCaseStr())
    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])





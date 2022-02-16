# DSC 510
# Week 5
# Programming Assignment Week 5.1
# Author Michael Ersevim
# 7/8/2021

'''Purpose of code is to get at least two numbers from the user and perform a particular operation on those numbers.
Also need to error check inputs and handle string of variable length for average using While loop
'''

operand = "" #initializing variables at the start
inp1 = 0
inp2 = 0
ans = 0

def calculateAverage(): # define the average calculation
    avgnum = inp1 + inp2
    smavg = 0 #initializes locally the next three vars
    count = 0
    sampleavg = 0

    while avgnum >= 0: #if a negative number is entered, it will reak out of the while loop
        avgnum = float(input("Enter a number from your list. If finished, enter a negative number: "))
        if avgnum < 0: #negative check to break out
            break
        smavg = smavg + avgnum #updating the roling total
        count = count + 1 # increment count
        sampleavg = float(smavg / count) #do the calc
    print('The average of your numbers is: ', sampleavg) #give the answer

def performCalculation(operand): #main welcome and input if using operator (not average)
    operand = str(input('You can enter "+", "-", "*" or "/" for any two numbers, OR type "avg" for the average value of a list of two or more numbers: '))
    if operand == "avg": #if average is desired, exits out to average function
         calculateAverage()
    elif operand == "Avg":
         calculateAverage()
    elif operand == '+': # a bit redundant, but doing the other 4 operations
        inp1 = float(input("Now enter the first number you'd like to perform the operation on: "))
        inp2 = float(input("Now enter the second number you'd like to perform the operation on: "))
        ans =  inp1 + inp2
        print(ans)
    elif operand == '-':
        inp1 = float(input("Now enter the first number you'd like to perform the operation on: "))
        inp2 = float(input("Now enter the second number you'd like to perform the operation on: "))
        ans =  inp1 - inp2
        print(ans)
    elif operand == '*':
        inp1 = float(input("Now enter the first number you'd like to perform the operation on: "))
        inp2 = float(input("Now enter the second number you'd like to perform the operation on: "))
        ans =  inp1 * inp2
        print(ans)
    elif operand == '/':
        inp1 = float(input("Now enter the first number you'd like to perform the operation on: "))
        inp2 = float(input("Now enter the second number you'd like to perform the operation on: "))
        ans =  inp1 / inp2
        print(ans)
    else:
        print('Please select a valid operator!') #error check for a valid operator
        performCalculation(operand)

print('Hello! This program will add, subtract, multiply or divide any two numbers you enter.') #Welcome and description

performCalculation(operand) #calls the main function defined above

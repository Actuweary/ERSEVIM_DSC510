# DSC 510
# Week 5
# Programming Assignment Week 5.1
# Author Michael Ersevim
# 7/8/2021

'''Purpose of code is to get at least two numbers from the user and perform a particular operation on those numbers.
Also need to error check inputs and handle string of variable length for average using While loop
'''

inp1 = 0
inp2 = 0

def calculateAverage():
    avgnum = 0
    smavg = 0
    count = 0
    sampleavg = 0

    while avgnum >= 0:
        avgnum = float(input("Enter another number from your list. If finished, enter a negative number: "))
        if avgnum < 0:
            break
        smavg = smavg + avgnum
        count = count + 1
        sampleavg = float(smavg / count)
    print('The average of your numbers is: ', sampleavg)


def performCalculation(operand):
    inp1 = float(input("Now enter the first number you'd like to perform the operation on: "))
    inp2 = float(input("Now enter the second number you'd like to perform the operation on: "))
    if operand == "+":
        return  inp1 + inp2
    elif operand == '-':
        return  inp1 - inp2
    elif operand == '*':
        return  inp1 * inp2
    elif operand == '/':
        return  inp1 / inp2
    elif operand == 'avg':
        return calculateAverage()
    elif operand == 'Avg':
        return  calculateAverage()
    else:
        print('Please make a valid selection!')

print('Hello! This program will add, subtract, multiply or divide any two numbers you enter.')
operand = str(input('You can enter "+", "-", "*" or "/" for any two numbers, OR type "avg" for the average value of a list of two or more numbers: '))

#inp1 = float(input("Now enter the first number you'd like to perform the operation on: "))
#inp2 = float(input("Now enter the second number you'd like to perform the operation on: "))
performCalculation(operand)

print(performCalculation(operand))


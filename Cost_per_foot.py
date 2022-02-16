# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Michael Ersevim
# 6/17/2021
'''Purpose of code is to welcome use, get name,
get amount of cable in feet and generate the
cost by multiplying by $0.87 per foot, and
print a receipt for the user with all the details
'''
compname = input('Hello! What is the name of your company? ') #ask for and assign name to var
cablelength = float(input('Now how many feet of cable would you like installed? ')) #float of feet
cost = 0.87 * cablelength # do the calc
formatted_cost = "{:.2f}".format(cost) # force the dollars to show two decimal places
print ('Here is your receipt,', compname) # print top of receipt with company name
print ('Your total cost for', cablelength, 'feet of fiber optic cable will cost $',formatted_cost) #show cost for length
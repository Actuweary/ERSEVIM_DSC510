# DSC 510
# Week 4
# Programming Assignment Week 4
# Author Michael Ersevim
# 7/2/2021

'''Purpose of code is to welcome use, get name,
get amount of cable in feet and generate the
cost by multiplying by $0.87 per foot up to 100ft,
$0.80 per foot up to 250 ft, and $0.50 for orders over 250 ft.
Lastly, print a receipt for the user with all the details.
This version will use a function with two parameters to calculate
the cost instead of using IF statements
'''
def cost(cpf, cablelength): #defining the cost function
    return cpf * cablelength  #returning the calculation

compname = input('Hello! What is the name of your company? ') #ask for and assign name to var
cablelength = float(input('Now how many feet of cable would you like installed? ')) #float of feet
if cablelength <=100:
    cpf = 0.87   # get the cost per foot for under 100 ft
elif cablelength >500:
    cpf = 0.50 # get the cost per foot for GT 500 ft
elif cablelength >250:
    cpf = 0.70  # get the cost per foot for between 250 - 500 ft
else:
    cpf = 0.80   # get the cost per foot for anything between 100 - 250 ft

formatted_cost = "${:.2f}".format(cost(cpf, cablelength)) # call the cost function and force USD format
print ('Here is your receipt,', compname) # print top of receipt with company name
print ('Your total cost for', cablelength, 'feet of fiber optic cable will cost', formatted_cost) #call the cost func which has been formatted in 'formatted_cost'
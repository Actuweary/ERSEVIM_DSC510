# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Michael Ersevim
# 6/24/2021
'''Purpose of code is to welcome use, get name,
get amount of cable in feet and generate the
cost by multiplying by $0.87 per foot up to 100ft,
$0.80 per foot up to 250 ft, and $0.50 for orders over 250 ft.
Lastly, print a receipt for the user with all the details
'''
compname = input('Hello! What is the name of your company? ') #ask for and assign name to var
cablelength = float(input('Now how many feet of cable would you like installed? ')) #float of feet
if cablelength <=100:
    cost = 0.87 * cablelength  # do the calc for under 100 ft
elif cablelength >500:
    cost = 0.50 * cablelength # do the calc for GT 500 ft
elif cablelength >250:
    cost = 0.70 * cablelength # do the calc for between 250 - 500 ft
else:
    cost = 0.80 * cablelength  # do the calc for anything between 100 - 250 ft

formatted_cost = "{:.2f}".format(cost) # force the dollars to show two decimal places
print ('Here is your receipt,', compname) # print top of receipt with company name
print ('Your total cost for', cablelength, 'feet of fiber optic cable will cost $',formatted_cost) #show cost for length
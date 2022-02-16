# DSC 510
# Week 10
# Programming Assignment Week 10.2
# Author Michael Ersevim
# 8/12/2021

'''Purpose of code is to demonstrate the ability to create a class and objects
with inheritance in a simple cash register schema'''

class CashRegister: #defines CLass
    def __init__(self):
        self.total = 0.00 #initializes variables as float
        self.count = 0

    def add_items(self,num_items,price_items): #child class for adding items
        self.count = self.count + num_items
        self.total = self.total + price_items

    def get_total(self,price_items): #child class for getting the total cost items
        return self.total

    def get_count(self,num_items): #child class for counting items
        return self.count

    def clearCart(self): #clears cart
        self.total = 0.00
        self.count = 0

def go_again(register,price_items,num_items): # the loop for adding items, clearing cache or quitting
    YorN = input("Would you like to Add more items? (A), Clear your cart to start over (C), or Quit (Q)? ")
    if YorN == 'Q' or YorN == 'q': #quits program
        print("Thanks for using my simple register!")
        exit()
    elif YorN == 'A' or YorN == 'a': #calls additional section
        additional(register)
    elif YorN == 'C' or YorN == 'c': #clears cart and starts again
        register.clearCart()
        main()
    else:
        print("Invalid entry!") #if anything else is entered
        go_again(register,price_items,num_items)

def main(): #the main body of the program
    register = CashRegister() #register takes on the attributes of the Class from 'CashRegister
    num_items = int(input("How many items are you adding to you cart? "))
    price_items = float(input("What is the price of the items that you added? "))
    register.add_items(num_items,price_items) #adds items - loop to add many items if need be
    print("Your total cost is:", "${:.2f}".format(register.get_total(price_items))) #cost in USD
    print("Your total item count is:", register.get_count(num_items)) #counts items
    go_again(register,price_items,num_items) #asks if you want to do more items

def additional(register): #if adding anything else
    num_items = int(input("How many items are you adding to you cart? "))
    price_items = float(input("What is the price of the items that you added? "))
    register.add_items(num_items,price_items) #adds items - loop to add many items if need be
    print("Your total cost is:", "${:.2f}".format(register.get_total(price_items)))#cost in USD
    print("Your total item count is:", register.get_count(num_items))
    go_again(register,price_items,num_items) #asks if you want to do more items

if __name__ == "__main__": #good practice to use this setup
    main()
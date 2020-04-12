# shopping_cart.py



products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017



# TODO: write some Python code here to produce the desired output
import datetime
import time
from datetime import datetime
from time import strftime
now=datetime.now()
checkouttime= now.strftime("%m/%d/%Y %I:%M %p") #programiz.com --> current datetime
userreceipt =[]
productlist= ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
subtotal=0
total=0
taxpercentage=0.0875
def print_rinfo:    #defining the receipt info
    print("---------------------------------")
    print("Carl's Consumables")
    print("---------------------------------")
    print("Phone Number: (202)-699-2045")
    print("---------------------------------")
    print("Checkout date: " + checkouttime)
    print("---------------------------------")
    print("---------------------------------")
    print("Purchased Products: ")


while True:
    userproduct= (input("Please input the product identifier: "))
    userreceipt.append(userproduct) #put this at the end
    if userproduct.upper() == ("DONE"): #it has to be done and gotta do .upper but put this if first before everything else
        userreceipt=userreceipt[:-1] #found a page on stackoverflow on it
        print("---------------------------------")
        print("Carl's Consumables")
        print("---------------------------------")
        print("Phone Number: (202)-699-2045")
        print("---------------------------------")
        print("Checkout date: " + checkouttime)
        print("---------------------------------")
        print("---------------------------------")
        print("Purchased Products: ")
        for userproduct in userreceipt: #everything in the for statement is based on Professor Rosetti's walkthrough
            receiptproduct=[i for i in products if str(i["id"]) == str(userproduct)]
            receiptproduct=receiptproduct[0]
            subtotal =subtotal+receiptproduct["price"]
            priceusd= (receiptproduct["price"])
            print("..." + receiptproduct["name"] + " ($" + "{0:.2f}".format(priceusd) + ")")
        print("---------------------------------")   
        taxtotal= subtotal*taxpercentage
        total= float(subtotal)+float(taxtotal) 
        subtotalformated= "{0:.2f}".format(subtotal)
        taxformated= "{0:.2f}".format(taxtotal)
        totalformated= "{0:.2f}".format(total)
        print ("Subtotal: $" + str(subtotalformated))
        print ("Tax: $" + str(taxformated))
         
        print ("Total: $"+ str(totalformated))
         
        print("---------------------------------")
        print("Thanks please come again soon!")
        print("---------------------------------")
        break
    elif ((userproduct)) not in str(productlist) or int(userproduct)==0:
        print ("Ensure it is a valid product identifier")
        userreceipt=userreceipt[:-1]
    
    
    
  





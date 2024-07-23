from datetime import datetime #importing datetime from datetime
from read import * #importing all the function of read.py module
from write import * #importing all the function of write.py module

#creating a welcome display message
def heading(company_name):
    print("-" * 184)
    print(f" \t \t \t \t \t \t \t Welcome to {company_name}!")
    print("-" * 184)
    print("\n")

#options to choose from.
def menu():
    print("Things you can do in our system. Choose according to your wish.")
    print("1. Buy from Laptronic")
    print("2. Restock for your company")
    print("3. Exit")
    print("\n")

#product details heading
def product_details():
    print("\t\t\t\t\t\t\t\t PRODUCT DETAILS")
    print("-" * 184)
    print("ID  \t Product name \t  Brand \t Price \t  Quantity  \t Processor Details \t Graphic Card")
    print("-" * 184)

#validating ID and aslo using try except
def validate_id(dic):
    valid = False
    while valid == False:
            try:
                laptop_id = int(input("Enter the ID of the laptop you want to purchase:"))
                while laptop_id<= 0 or laptop_id > len(dic):
                    print("INVALID ID! Please provide a valid ID.")
                    print("\n")
                    laptop_id = int(input("Enter the ID of the laptop you want to purchase:"))
                valid = True
            except:
                print("Do not enter Characters!!!!")
                print("Please Enter Numbers only.")
    return laptop_id

#validating quantity and also using try except
def validate_quantity(dic, laptop_id):
    valid = False
    while valid == False:
            try:
                laptop_quantity= int(input("Enter the quantity of the laptop of you want to purchase:"))
                while laptop_quantity <= 0 or laptop_quantity > int(dic[laptop_id][3]):
                    print("INVALID ID! Please provide a valid ID.")
                    print("\n")
                    laptop_quantity= int(input("Enter the quantity of the laptop of you want to purchase:"))
                valid = True
            except:
                print("Do not enter Characters!!!!")
                print("Please Enter Numbers only.")
    return laptop_quantity

#validating quantity for the purchase and also using try and except
def validate_quantity_purchase(dic, laptop_id):
    valid = False
    while valid == False:
            try:
                laptop_quantity= int(input("Enter the quantity of the laptop of you want to purchase:"))
                while laptop_quantity <= 0:
                    print("INVALID ID! Please provide a valid ID.")
                    print("\n")
                    laptop_quantity= int(input("Enter the quantity of the laptop of you want to purchase:"))
                valid = True
            except:
                print("Do not enter Characters!!!!")
                print("Please Enter Numbers only.")
    return laptop_quantity



#Function to Calculate Sales for a Specific Customer and Quantity
def sales(dic, customer_id, customer_quantity):
    product_name = dic[customer_id][0]
    selected_quantity = customer_quantity
    unit_price = dic[customer_id][2]
    selected_quantity_price = dic[customer_id][2].replace("$", '')
    total_price = int(selected_quantity_price) * int(selected_quantity)
    return product_name, selected_quantity,unit_price, total_price

#Function that collects customer details
def customer_details():
    print("-" * 184)
    print("To generate a bill, provide the details: ")
    print("-" * 184)
    print("\n")
    name = input("enter the name of the Customer: ")
    print("\n")
    phone= input("enter the phone number of the Customer: ")
    print("-" * 184)
    print("\n")
    print("-" * 184)
    print("\n")
    return name, phone


#function to Calculate purchase for a Specific Customer and Quantity
def purchase(dic, company_id,company_quantity):
        product_name = dic[company_id][0]
        selected_quantity = company_quantity
        unit_price = dic[company_id][2]
        selected_quantity_price = dic[company_id][2].replace("$", '')
        total_price = int(selected_quantity_price) * int(selected_quantity)
        return product_name, selected_quantity, unit_price, total_price


#Function that collects company details
def company_details():
    print("-" * 184)
    print("To generate a bill, provide the details: ")
    print("-" * 184)
    print("\n")
    name = input("enter the name of the company: ")
    print("\n")
    phone = input("enter the phone number of the company: ")
    print("-" * 184)
    print("\n")
    print("-" * 184)
    print("\n")
    return name, phone










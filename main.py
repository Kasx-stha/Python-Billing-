from datetime import datetime #importing datetime from datetime
from operations import* #importing all the function of operations.py module
from read import * #importing all the function of read.py module
from write import * #importing all the function of write.py module

#importing heading from opertaions.py
heading ("System")

#importimg create_file from read.py
dic = create_file()
loop = True
while loop == True:
    menu()
    #using try and except to manage errors
    s= False
    while s== False:
        try:
            option = int(input("Choose a option: "))
            s= True
        except ValueError:
            print("Please enter the numbers only!!")
        print("\n")

    if option == 1:
        # importing heading from opertaions.py
            heading("Laptronic")

            #creating empty list
            laptop_sold = []
            more_products = True
            while more_products == True:
                #importing product_details from opertaions.py
                product_details()

                #importing read_file from read.py
                read_file()
                while True:
                #Validating id
                    customer_id = validate_id(dic)
                    if int(dic[customer_id][3]) <= 0:
                        print("OUT OF STOCK")
                        print("\n")
                    else:
                        customer_quantity = validate_quantity(dic, customer_id)
                        break

                #importing update_sfile from write.py
                update_sfile(customer_id, customer_quantity, dic)

                #importing sales from opertaions.py
                product_name, selected_quantity, unit_price, total_price = sales(dic, customer_id, customer_quantity)

                #adding the parameter value in laptop sold list
                laptop_sold.append([product_name, selected_quantity, unit_price, total_price])

                #asking the customer wether they want to continue or not
                customer_request = input("Do you want to continue (Y/N)?").upper()
                print("\n")
                if customer_request == "Y":
                            more_products = True
                else:
                            total = 0
                            for i in laptop_sold:
                                total += int(i[3])
                            grand_total = total + shippingcharge(15, 10)
                            dateandtime_atm = datetime.now()
                            #implementating date and time
                            a = str(dateandtime_atm).split(" ")
                            b = "_".join(a)
                            c = b.replace(":", "_")

                            #importing customer_details from operations.py
                            name,phone = customer_details()

                            #importing print_sales from write.py
                            print_sales(name, phone, dateandtime_atm, total, shippingcharge, grand_total, laptop_sold)

                            # calling the function from write.py module and it prints bill in file
                            sales_txtfile(name,c, phone, dateandtime_atm, total, shippingcharge, grand_total, laptop_sold)

                            #loop = False
                            more_products = False
    elif option == 2:
            #importing heading from operations.py
            heading("Manufacturer")
            #list
            laptop_bought=[]

            more_products = True
            while more_products == True:
                #importing product_details from operations.py
                product_details()

                #importing read_file from read.py
                read_file()
                company_id = validate_id(dic)
                company_quantity = validate_quantity_purchase(dic, company_id)
                    #importing update_pfile from write.py
                update_pfile(company_id, company_quantity, dic)

                #importing purchase from operations.py
                product_name, selected_quantity, unit_price, total_price= purchase(dic, company_id, company_quantity)

                    #adding the parameters in list laptop_bought
                laptop_bought.append([product_name, selected_quantity, unit_price, total_price])

                    #asking the suer if they want to continue or not
                company_request = input("Do you want to continue (Y/N)?").upper()
                print("\n")

                if company_request == "Y":
                        more_products = True
                else:
                        total = 0
                        VAT = 0.13 * total_price

                        for i in laptop_bought:
                            total += int(i[3])
                        grand_total = total + VAT
                        dateandtime_atm = datetime.now()
                        a = str(dateandtime_atm).split(" ")
                        b = "_".join(a)
                        c = b.replace(":", "_")

                        #importing company_details from operations
                        name, phone = company_details()

                        # calling the function from write.py module and it prints bill in shell
                        print_purchase(name, phone, dateandtime_atm, total, VAT, grand_total, laptop_bought)

                        # calling the function from write.py module and it prints bill in file
                        purchase_txtfile(name,c, phone, dateandtime_atm, total, VAT, grand_total, laptop_bought)

                        #loop = false
                        more_products = False

    elif option == 3:
            loop = False
            print("Thank you for visiting our system. \nHope you enjoyed it. ")
            print("You exited the system")
            print("\n")

    else:
            print("Your option", option, "does not match. Please try again.")
            print("\n")




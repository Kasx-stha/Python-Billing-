#updating quantity of laptops after deducting customer quantity in text file.
def update_sfile(customer_id,customer_quantity,dic):
    dic[customer_id][3] = int(dic[customer_id][3]) - int(customer_quantity)
    file = open("Laptop.txt", "w")
    for values in dic.values():
        file.write(
            str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(
                values[4]))
        file.write("\n")
    file.close()
    return customer_id

#printing the bill of sell in shell
def print_sales(name, phone, dateandtime_atm,total,shippingcharge,grand_total, laptop_sold):
    print("\n")
    print("\t \t \t \t \t \t \t Laptronic Bill")
    print("\n")
    print("\t \t \t Swoyambhu , Kathmandu | Phone no: 9844447777")
    print("\n")
    print("- " * 184)
    print("Customer details are: ")
    print("-" * 184)
    print("Customer's Name: " + str(name))
    print("Contact number: " + str(phone))
    print("Date and time of purchase: " + str(dateandtime_atm))
    print("-" * 184)
    print("\n")
    print("Purchase Details are: ")
    print("-" * 184)
    print("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
    print("-" * 184)
    for i in laptop_sold:
        print(i[0], "\t\t\t", i[1], "\t\t\t\t\t ", i[2], "\t\t\t\t\t", "$", i[3])
    print("-" * 184)
    print("Your total is : $" + str(total))
    print("Your Shipping charge is : $", shippingcharge(15, 10))
    print("Grand Total : $" + str(grand_total))
    print("THANK YOU FOR CHOOSING US!!")
    print("\n")

#printing the bill of sell in text file
def sales_txtfile(name,c, phone, dateandtime_atm,total,shippingcharge,grand_total, laptop_sold):
    file = open(str(name) + "_"+str(c) + "Laptop.txt", "w")
    file.write("\n")
    file.write("\t \t \t \t \t  Laptronic Bill")
    file.write("\n")
    file.write("\t \t \t Swoyambhu , Kathmandu | Phone no: 9844447777")
    file.write("\n")
    file.write("-" * 150)
    file.write("\n")
    file.write("Customer details are: ")
    file.write("\n")
    file.write("-" * 150)
    file.write("\n")
    file.write("Customer's Name: " + str(name))
    file.write("\n")
    file.write("Contact number: " + str(phone))
    file.write("\n")
    file.write("Date and time of purchase: " + str(dateandtime_atm))
    file.write("\n")
    file.write("-" * 150)
    file.write("\n")
    file.write("Purchase Details are: ")
    file.write("\n")
    file.write("-" * 150)
    file.write("\n")
    file.write("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
    file.write("\n")
    for i in laptop_sold:
        file.write(
            str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t\t " + str(i[2]) + "\t\t\t\t" + "$" + str(
                i[3]) + "\n")
    file.write("-" * 150)
    file.write("\n")
    file.write("Your total is : $" + str(total))
    file.write("\n")
    file.write("Your Shipping charge is : $ "+ str(shippingcharge(15, 10)))
    file.write("\n")
    file.write("Grand Total : $" + str(grand_total))
    file.write("\n")
    file.write("THANK YOU FOR CHOOSING US!!!")
    file.close()

#updating the of purchased laptop after adding user_quantity in text file
def update_pfile(company_id, company_quantity, dic):
        dic[company_id][3] = int(dic[company_id][3]) + int(company_quantity)
        file = open("Laptop.txt", "w")
        for values in dic.values():
            file.write(
                str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(
                    values[4]))
            file.write("\n")
        file.close()
        return company_id

#printing the bill of purchase in shell
def print_purchase(name, phone, dateandtime_atm,total,VAT,grand_total, laptop_bought):
    print("\n")
    print("-" * 184)
    print("\n")
    print("\t \t \t \t \t \t \t Manufacturer Bill")
    print("\n")
    print("\t \t \t Kalanki, Kathmandu | Phone no: 987777444")
    print("\n")
    print("- " * 184)
    print("Company details are: ")
    print("-" * 184)
    print("Company Name: " + str(name))
    print("Company contact number: " + str(phone))
    print("Date and time of purchase: " + str(dateandtime_atm))
    print("-" * 184)
    print("\n")
    print("Purchase Details are: ")
    print("-" * 184)
    print("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
    print("-" * 184)
    for i in laptop_bought:
        print(i[0], "\t\t\t", i[1], "\t\t\t\t ", i[2], "\t\t\t\t", "$", i[3])
    print("-" * 184)
    print("Your total is : $" + str(total))
    print("Your VAT is : $", VAT)
    print("Grand Total : $" + str(grand_total))
    print("\n")

#printing the bill of purchase in text file
def purchase_txtfile(name,c, phone, dateandtime_atm,total,VAT, grand_total, laptop_bought):
    file = open(str(name) + "_"+ str(c) + ".txt", "w")
    file.write("\n")
    file.write("\t \t \t \t \t \t Manufacturer Bill")
    file.write("\n")
    file.write("\t \t \t Kalanki , Kathmandu | Phone no: 987774444")
    file.write("\n")
    file.write("-" * 150)
    file.write("\n")
    file.write("Company details are: ")
    file.write("\n")
    file.write("-" * 150)
    file.write("Company Name: " + str(name))
    file.write("\n")
    file.write("Company contact number: " + str(phone))
    file.write("\n")
    file.write("Date and time of purchase: " + str(dateandtime_atm))
    file.write("\n")
    file.write("-" * 150)
    file.write("\n")
    file.write("Purchase Details are: ")
    file.write("\n")
    file.write("-" * 150)
    file.write("\n")
    file.write("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
    file.write("\n")
    file.write("-" * 150)
    for i in laptop_bought:
        file.write(str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t\t " + str(i[2]) + "\t\t\t\t" + "$" + str(
            i[3]) + "\n")
    file.write("-" * 150)
    file.write("\n")
    file.write("Your total is : $" + str(total))
    file.write("\n")
    file.write("Your VAT is : $ " + "" + str(VAT) )
    file.write("\n")
    file.write("Grand Total : $" + str(grand_total))
    file.write("\n")
    file.close()


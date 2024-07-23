#creating a file "Laptop.txt" and keeping it in a function
def create_file():
    file = open("Laptop.txt", "r")
    dic = {}
    list_id = 1
    for line in file:
        line = line.replace("\n", "")
        dic.update({list_id: line.split(",")})
        list_id = list_id + 1
    file.close()
    return dic

#reading from the file "Laptop.txt"
def read_file():
    file = open("Laptop.txt", "r")
    a = 1
    for line in file:
        print(a, "\t\t" + line.replace(",", "\t\t"))
        a = a + 1
    print("-" * 184)
    file.close()
    print("\n")

#using function for calculating shipping charge
def shippingcharge(a,b):
    mutliply = a * b
    return mutliply


#Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.
prods = [["omo","30kshs",300], ["milk","50kshs",200],["bread","45kshs",359], ["coffee","5kshs",79]]
stock=float((prods[0][2])+(prods[1][2])+(prods[2][2])+(prods[3][2]))
print(stock)
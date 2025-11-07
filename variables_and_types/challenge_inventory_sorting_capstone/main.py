# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
#items split
candy1 =  items[0:9]
candy2 = items[11:20]
dry_goods = items[22:27]
# catagories split
catergory1 = categories[0:11]
catergory2 = categories[12:24]
#prices
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
print("We have"+" "+candy1+" "+"for"+" "+bubblegum_price+" "+"in the"+" "+catergory1)

print("We have"+" "+candy2+" "+"for"+" "+chocolate_price+" "+"in the"+" "+catergory1)

print("We have"+" "+dry_goods+" "+"for"+" "+pasta_price+" "+"in the"+" "+catergory2)
#iniitial lists
meat = ["Ham", 3.99 , 50,"sliced"]
print(meat)
cheese = ["cheddar", 5.49, 100, "sharp"]
print(cheese)
condiment = ["Mustard", 1.99, 75, "Spicy"]
print(condiment)

#main 
deli_dept = [meat, cheese, condiment]
print("Initial deli list:", deli_dept)

#Restocking
if meat[0] == "Ham" and meat[2] <100:
    meat[2] = 100

#Seasonal Meats
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
print(seasonal_meat)
deli_dept.append(seasonal_meat)
print(deli_dept)
deli_dept.remove(condiment)
print(deli_dept)
deli_dept.sort()
print(deli_dept)

print("Updated Deli List:", deli_dept)
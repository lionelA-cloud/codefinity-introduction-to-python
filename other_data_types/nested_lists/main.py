#lists
vegetables = ["tomatoes", "potatoes", "onions"]
print(vegetables)
vegetables.remove("onions")
print(vegetables)
vegetables.append("carrots")
print(vegetables)
vegetables.append("cucumbers")
print(vegetables)
vegetables.sort()
print(vegetables)

print("Updated Vegetable Inventory:", vegetables)

if "carrots" not in vegetables:
    vegetables.append("carrots")
    
    print("Carrots are already in the list.")

if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
    
    print("Cucumbers are already in the list.")

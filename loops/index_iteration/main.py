prices = [29.99, 45.50, 12.75, 38.20]

#Discount by Position
#Apply discount percentages to product prices based on their position in the list 
for index in range(len(prices)):
    if index == 0:
          factor = 0.90   # 10% off
    elif index == 1:
        factor = 0.80   # 20% off
    elif index == 2:
        factor = 0.85   # 15% off
    elif index == 3:
        factor = 0.95   # 5% off

# 2. Apply the factor
    prices[index] *= factor

    print(f"Updated price for item {index}: ${prices[index]:.2f}")


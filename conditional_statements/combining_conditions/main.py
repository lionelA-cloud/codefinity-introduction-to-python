# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = True

movingProduct = discounted or lowStock

promotion = not movingProduct

message = print("Is the item eligible for promotion?", promotion)


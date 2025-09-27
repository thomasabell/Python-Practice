package_price = 99

quantity = int(input("Please enter the number of packages purchased: "))

if quantity < 1:
    print("Error: Quantity must be greater than 0.")
    
else:
    if quantity >= 10:
        if quantity <= 19:
            discount_rate = 0.10
        elif quantity <= 49:
            discount_rate = 0.20
        elif quantity <= 99:
            discount_rate = 0.30
        else:
            discount_rate = 0.40
    else:
        discount_rate = 0.0

    subtotal = quantity * package_price
    discount = subtotal * discount_rate
    total = subtotal - discount

    print("Subtotal: $" + str(subtotal))
    print("Discount: " + str(discount_rate * 100) + "%")
    print("Total After Discount: $" + str(total))
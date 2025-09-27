weight = float(input("Please enter the weight of your package: "))

if weight <= 0:
    print("Error, please enter a valid package weight.")
else:
    if weight <= 2:
        rate = 1.50
    else:
        if weight <= 6:
            rate = 3.00
        else:
            if weight <= 10:
                rate = 4.00
            else:
                rate = 4.75

    shipping_charge = weight * rate
    print(f"Your total shipping charge is: ${shipping_charge:.2f}")

color1 = input("Please enter a primary color: ")
color2 = input("Please enter another primary color: ")

if color1 not in ("red", "blue", "yellow") or color2 not in ("red", "blue", "yellow"):
    print("Error: You must enter red, blue, or yellow for color 1 and 2.")

elif color1 == color2:
    print("You entered the same color twice. Your result is still " + color1 + ".")

elif color1 == "red" and color2 == "blue" or color1 == "blue" and color2 == "red":
    print("The secondary color is purple.")
elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue":
    print("The secondary color is green.")
elif color1 == "red" and color2 == "yellow" or color1 == "yellow" and color2 == "red":
    print("The secondary color is orange.")

month = int(input("Please input your birth month (1-12): "))
day = int(input("Please input your birth day: "))
year = int(input("Please input a two digit birth year: "))

if month * day == year:
    print("Congrats, your birthday is a magic date!")
else:
    print("Sorry, your birthday is not a magic date.")
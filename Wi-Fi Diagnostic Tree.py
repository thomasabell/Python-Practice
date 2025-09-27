print("Welcome to the Wi-Fi troubleshooter! \n")

step1 = input("First, try rebooting the computer and try to connect again. Did that fix the problem? (yes or no) ").lower()
if step1 == "yes":
    print("Great, you are now connected to the Wi-Fi")
else:
    step2 = input("Okay, reboot the router and try to connect. Did that fix the problem? (yes or no) ").lower()
    if step2 == "yes":
        print("Okay, you are now connected to the Wi-Fi")
    else:
        step3 = input("Make sure the cables between the router and modem are plugged in firmly. Did that fix the problem? (yes or no) ").lower()
        if step3 == "yes":
            print("Okay, you are now connected to the Wi-Fi")
        else:
            step4 = input("Move the router to a new location and try to connect. Did that fix the problem? (yes or no) ").lower()
            if step4 == "yes":
                print("Okay, you are now connected to the Wi-Fi")
            else:
                print("You may need to get a new router. Thank you for using the Wi-Fi troubleshooter.")

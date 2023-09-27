# program to check if the entered year is a leap year or not

print("------------------------------------------")

year = int(input("Enter Year: "))

if year % 4 == 0 or year % 100 == 0 or year % 400 == 0 :
    print("It's a Leap Year! :D")

else:
    print("It's Not a Leap Year. :(")


# program to convert the height in inches and feet from centimeters


cm = float(input("Enter Hight in Centimeters: "))

inches = 0.394 * cm
feet = 0.0328 * cm

print( inches)

print("The length in inches",round(inches,2))

print("The length in feet",round(feet,2))



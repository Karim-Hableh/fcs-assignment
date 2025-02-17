age = int(input("Enter your age: "))
if age < 5:
    print("The ticket price is Free")
elif 5 <= age <= 12:
    print("The ticket price is $5")
elif 13 <= age <= 59:
    print("The ticket price is $10")
else:  # Age 60 and above
    print("The ticket price is $7")
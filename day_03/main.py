print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
if (height <= 120):
    print("Sorry you have to grow taller before you can ride.")
else:
    age = int(input("What is your age? "))
    bill = 0
    if (age <= 12):
        print("Child tickets are $5.")
        bill += 5
    elif (age >= 18):
        print("Adult tickets are $12.")
        bill += 12
    else:
        print("Youth tickets are $7.")
        bill += 7

    include_photo = input("Do you want to have photo take? Type Y for Yes and N for No.").lower()
    if (include_photo == "y"):
        bill += 3

    print(f"Total bill is ${bill}")

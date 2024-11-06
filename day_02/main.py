print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
num_of_people = float(input("How many people to split the bill? "))

result = (total_bill * (1 + tip / 100)) / num_of_people

print(f"Each person should pay: ${result:0.2f}")
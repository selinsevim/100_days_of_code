print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

one_person_price = (bill / people) * ((tip + 100) / 100)
print(round(one_person_price, 2))



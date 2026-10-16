import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# select randomly and add to the list
# at the end combine it
letter_list = []
number_list = []
symbols_list = []
password = ""

# Randomly select the letters from the list
for number in range(1, nr_letters+1):
    random_letter = random.choice(letters)
    letter_list.append(random_letter)

print(letter_list)

# Randomly select the numbers from the list
for number in range(1, nr_numbers+1):
    random_number = random.choice(numbers)
    number_list.append(random_number)

print(number_list)

# Randomly select the symbols from the list
for number in range(1, nr_symbols+1):
    random_symbol = random.choice(symbols)
    symbols_list.append(random_symbol)

print(symbols_list)

# Combine the password
password = letter_list + number_list + symbols_list
print(password)
random.shuffle(password)

single = ""

for element in password:
    single += element

print(single)
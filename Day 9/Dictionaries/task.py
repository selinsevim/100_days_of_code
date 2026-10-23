programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Get the certain value of a key in dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Adding new key:value pair to the dictionary
programming_dictionary["Loop"] = "A programming structure that repeats a set of instructions until a specific ending condition is met."
print(programming_dictionary)

# Empty the dictionary
# programming_dictionary = {}

# Loop through the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
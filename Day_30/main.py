# Error handling
try:
    file = open("/Users/selinsevim/Documents/100_days_of_code/Day_30/data.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("/Users/selinsevim/Documents/100_days_of_code/Day_30/data.txt", "w")
except KeyError as error:
    print(f"That key {error} does not exist")
else:
    content = file.read()
    print(content)
finally:
    # finally runs no matter what, no matter it succeeds or fails
    file.close()
    print("File is closed")
    raise TypeError("There is a type error")  # you can raise your own error

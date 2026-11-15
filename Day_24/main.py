# OPTION 1:

# # First you need to open the file in order to do some actions
# file = open(r"Day_24/my_file.txt")
# # You can read the file
# contents = file.read()
# print(contents)
# # You have to close the file because the computer reserves some resources for it
# file.close()

# OPTION 2:
# With this you dont need to close the file
with open(r"Day_24/my_file.txt") as file:
    # Save the content of the file into variable
    contents = file.read()
    print(contents)

# WRITE INTO THE FILE - this completely deletes the former texts
# with open(r"Day_24/my_file.txt", mode="w") as file:
#     file.write("New text")

# APPEND INTO THE FILE
with open(r"Day_24/my_file.txt", mode="a") as file:
    file.write("\nNew text")

# IF THE FILE DOESNT EXIST, AND THE MODE IS WRITE
# IT WILL CREATE A NEW FILE
with open(r"Day_24/new_file.txt", mode="w") as file:
    file.write("New text.")

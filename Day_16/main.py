from turtle import Turtle, Screen
from prettytable import PrettyTable

# # Creating objects
# timmy = Turtle()
# # Methods of Turtle class
# timmy.shape("turtle")
# timmy.color("CornflowerBlue")
# timmy.forward(100)
# timmy.circle(50)


# # Create screen object
# my_screen = Screen()

# # Printing the attributes of Screen
# print(my_screen.canvheight)
# # Creating methods
# my_screen.exitonclick()

# Create an object from PrettyTable class
table = PrettyTable()

# To add columns, use field_names attribute
table.field_names = ["Pokemon Name", "Type"]

# To add rows, use add_row method
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squitle", "Water"])
table.add_row(["Charmander", "Fire"])

# Change the style of table with an attribute
table.border = False
print(table)

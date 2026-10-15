friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# first randomize the number
import random
random_number = random.randint(0, 4)
print(random_number)
# use that number as an index
friend = friends[random_number]
print(friend)
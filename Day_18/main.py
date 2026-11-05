class User:
    # Constructor for attributes
    # Variables that are related to the objects
    # these are the attributes that you initialize the object with
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "Selin")
print(user_1.username)
print(user_1.followers)

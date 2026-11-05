class User:
    # Constructor for attributes
    # Variables that are related to the objects
    # these are the attributes that you initialize the object with
    # self here represents the object, so whenever a new method is created you call with the object -> self
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Selin")
user_2 = User("002", "Matthias")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#Understanding Classes

#how to build a class in Python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.followers = 0
        self.following =  0

    def follow(self, user):
        user.followers += 1
        self.following += 1




User1 = User("Udochukwu", "Udochukwu@gmail.com")
User2 = User("Chidera", "ehehehh@gmail.com")

User1.follow(User2)
print(User1.following)
print(User2.following)
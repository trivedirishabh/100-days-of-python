class User:
    def __init__(self,id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Rishabh")
user2 = User("002", "Rishi")

user1.follow(user2)

print(user1.followers)
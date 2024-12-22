class User:
  def __init__(self,user_id,username):
    self.user_id = user_id
    self.username = username
    self.followers = 0
    self.following = 0
    #print("this is a test")

  def follow(self,user):
    user.followers += 1
    self.following += 1

user1 = User("001", "clinton")
user2 = User("002", "Lucas")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user1.followers)
print(user1.following)
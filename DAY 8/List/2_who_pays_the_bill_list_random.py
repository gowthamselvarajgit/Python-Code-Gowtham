import random

friends = ["Gowtham", "Mahima", "Lordson", "Aarthi"]
size_of_list = len(friends)
random_number = random.randint(0,size_of_list-1)
print(friends[random_number])

#or

print(random.choice(friends))
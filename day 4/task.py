import random
import my_module
random_integer= random.randint(1,10)
print(random_integer)
print(my_module.clinton_fav_number)
random_float = random.random()
print(random_float)
uniform_random_number =  random.uniform(1,10)
print(uniform_random_number)

head_tail_generator = random.randint(1,2)
if head_tail_generator == 1:
  print("Heads")
else:
  print("Tails")
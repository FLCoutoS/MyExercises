#from: https://realpython.com/python3-object-oriented-programming/


import dog_father

dog = dog_father.Dog

# Instantiate the Dog ob# Class Attribute

philo = dog("Philo", 15)
mikey = dog("Mikey", 16)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))
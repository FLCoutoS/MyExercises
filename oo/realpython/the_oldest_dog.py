#from: https://realpython.com/python3-object-oriented-programming/
# Review exercises


import dog_father

dog = dog_father.Dog


# Instantiate the Dog object
jake = dog("Jake", 7)
doug = dog("Doug", 4)
william = dog("William", 5)


# Determine the oldest dog
def get_biggest_number(*args):
    return max(args)


# Output
print("The oldest dog is {} years old.".format(
    get_biggest_number(jake.age, doug.age, william.age)))
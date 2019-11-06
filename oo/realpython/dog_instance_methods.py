#from: https://realpython.com/python3-object-oriented-programming/


import dog_father

dog = dog_father.Dog

# instance method
def description(self):
    return "{} is {} years old".format(self.name, self.age)

# instance method
def speak(self, sound):
    return "{} says {}".format(self.name, sound)

# Instantiate the Dog object
mikey = dog("Mikey", 6)

# call our instance methods
print(mikey.description())
print(mikey.speak("Au Au Au"))
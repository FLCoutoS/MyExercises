#from: https://realpython.com/python3-object-oriented-programming/
"""
O bloco de códigos abaixo estava, originalmente, no arquivo 'dog_instance_methods.py', conforme
o exemplo no WebSite fonte deste exercício. Contudo, eu não consegui fazer funcionar após
importar a Classe Pai (dog_father). Estava ocorrendo erro de atributo: linha 20:
'o Objeto Dog não tem atributo description'.
Quando transferi o bloco de código para o arquivo da Classe Pai, FUNCIONOU.

# instance method
def description(self):
    return "{} is {} years old".format(self.name, self.age)

# instance method
def speak(self, sound):
    return "{} says {}".format(self.name, sound)
"""


import dog_father

dog = dog_father.Dog


# Instantiate the Dog object
mikey = dog("Mikey", 6)

# call our instance methods
print(mikey.description())
print(mikey.speak("Au Au Au"))
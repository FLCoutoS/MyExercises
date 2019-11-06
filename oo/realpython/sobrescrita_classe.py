#from: https://realpython.com/python3-object-oriented-programming/
#Substituindo a funcionalidade de uma classe pai
#As classes filho também podem substituir atributos e comportamentos da classe pai.
"""
A classe SomeBreed () herda as espécies da classe pai, enquanto a classe SomeOtherBreed ()
substitui as espécies, configurando-a para réptil.
"""


class Dog:
    species = 'mammal'

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = 'reptile'

frank = SomeBreed()
frank.species

beans = SomeOtherBreed()
beans.species
# Leituras realizadas sobre o tema em 21/10/2019
# PyDocs: PEP 202 -- List Comprehensions
# Disponível em: https://www.python.org/dev/peps/pep-0202/
# ========================================================

# ========================================================
# Artigo DataHackers: "Python: Dois truques geniais que ninguém te conta"
# Disponível em: https://medium.com/data-hackers/python-dois-truques-geniais-que-ningu%C3%A9m-te-conta-7ac99cef4c21
# ========================================================

# ========================================================

"""
PEP 202
A compreensão de lista fornece uma maneira mais concisa de criar listas
em situações em que map () e filter () e / ou loops aninhados seriam usados ​​atualmente.
"""

# Abordagem tradicional

lista = []  # criar a lista vazia

for numero in range(1, 10 + 1):  # range de 1 até 10+1 pois o python conta a partir do index 0
    triplo = numero * 3  # operação de triplicar
    lista.append(triplo)  # adicionar o resultado ao fim da lista

print(lista)  # exibir a lista

# Usando List Comprehenson

lista = [numero * 3 for numero in range(1, 10+1)]
print(lista)

# print([i for i in range(10)])





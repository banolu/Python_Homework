

frutas = ['platano', 'naranja', 'mango', 'limón'] # lista de frutas
verduras = ['Tomate', 'Patata', 'Repollo', 'Cebolla', 'Zanahoria'] # lista de verduras
productos_animales = ['leche', 'carne', 'mantequilla', 'yogur'] # lista de productos animales
tech_web = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB'] # lista de tecnologías web
paises = ['Méxicoia', 'Estonia', 'Dinamarca', 'Suecia', 'Noruega'] # lista de paises

# print las listas y su longitud
print('Frutas:', frutas)
print('Número de frutas:', len(frutas))
print('Verduras:', verduras)
print('Número de verduras:', len(verduras))
print('Productos animales:',productos_animales)
print('Número de productos animales:', len(productos_animales))
print('Tecnologías web:', tech_web)
print('Número de tecnologías web:', len(tech_web))
print('Países:', paises)
print('Número de países:', len(paises))

#Acceder a los elementos de la lista mediante la indexación positiva
#Accedemos a elemento de una lista utilizando su índice. Un índice de lista comienza desde 0.


primera_fruta = frutas[0] # estamos accediendo al primer elemento usando su índice
print(primera_fruta) # plátano
segunda_fruta = frutas[1]
print(segunda_fruta) # naranja
ultima_fruta = frutas[3]
print(ultima_fruta) # limón
# Último índice
last_index = len(frutas) - 1
ultima_fruta = frutas[last_index]


lista = ['item','item2','item3', 'item4', 'item5']
primer_item, segundo_item, tercer_item, *resto = lista
print(primer_item)     # item1
print(segundo_item)    # item2
print(tercer_item)     # item3
print(resto)           # ['item4', 'item5']
### Ejercicios



Lista = []; 
print("2.-",Lista)                                                              # 1 .- []
Alcalinos= ['sodio','potasio',{'celsio:55','rubidio:37'}, 11, 19];
print("5.-", Alcalinos)                                                         # 2.- ['sodio', 'potasio', {'rubidio:37', 'celsio:55'}, 11, 19]
print("3.-", len(Alcalinos))                                                    # 3.- 5

print("4.-", Alcalinos[0],",",Alcalinos[len(Alcalinos)//2],",",Alcalinos[-1])   # 4.- sodio , {'rubidio:37', 'celsio:55'} , 19                                                     
# medio = (len(Alcalinos)//2) ;                                        
# print(Alcalinos[medio])                                              
mixed_data_types=['Rodrigo','age','1.80','casado','Zacatecas' ]         
print("5.-",mixed_data_types)                                                   # 5.- ['Rodrigo', 'age', '1.80', 'casado', 'Zacatecas']
companies= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']  
                                                                                # 6.-


print("7.-",companies)                                                          #  7.- ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print("8.-",len(companies))                                                     #  8.- 7

companies[0] = 'Twitter'
print("10.- Elemento modificado:",companies[0] )
print("10.-" ,companies)                                                        # 10.-  ['Twitter', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 


companies.append('Facebook')                                                    # 11.- agrega un elemento al final de la lista companies
print("11.- El elemento agregado con append (al final) es:",companies[-1])  

companies.insert(3,'Inserto') ; print(companies)                                # 12.- Inserta un elemento en la lista despues del indice 3 
print("12.- Elemento insertado en la posicion 3 fue:",companies[3],". " ,  companies) 
                                                                                # 12.- Elemento insertado en la posicion 3 fue: Inserto .  ['Twitter', 'Google', 'Microsoft', 'Inserto', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Facebook']                             

companies[companies.index('IBM')+1]='cambiado'
print("13.- Se cambia elemento despues de IBM: Oracle por 'cambiado':", companies) 
                                                                                # 13.- Se cambia elemento despues de IBM: Oracle por 'cambiado'

print("15.- existe 'Oracle' dentro de companies?", 'Oracle' in companies)
                                                                                # 15.- existe 'Oracle' dentro de companies? False
print("16.- Cambia el orden de la lista con 'sorted'",sorted(companies))
                                                                                # 16.- Cambia el orden de la lista con ?sorted' ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'Inserto', 'Microsoft', 'Twitter', 'cambiado']
print(companies)
companies.reverse()
print("17.- Invierte horizontalmente la lista ",companies)
                                                                                # 17.- Invierte horizontalmente la lista  ['Facebook', 'Amazon', 'cambiado', 'IBM', 'Apple', 'Inserto', 'Microsoft', 'Google', 'Twitter']
rango_elementos_lista = companies[3:]
print("18.- Toma rango de elementos desde el 3 hasta el final '[3: ]'.",rango_elementos_lista)

                                                                                # 18.- Toma rango de elementos desde el 3 hasta el final '[3:]'. ['IBM', 'Apple', 'Inserto', 'Microsoft', 'Google', 'Twitter'] 

rango_elementos_lista = companies[:3]
print("19.- toma los primeros  3 elementos de la lista '[ :3]'.",rango_elementos_lista)
                                                                                # 19.- toma los primeros  3 elementos de la lista '[ :3]'. ['Facebook', 'Amazon', 'cambiado']
companies.pop(0)
print("21.- remueve el primer elemento de la lista con 'pop[0]'. ",companies)
print(companies)                                                                # 21 remueve el primer elemento de la lista con 'pop[0]'. 

companies.pop()                                                                 # 23.- Remueve el ultimo elemento de la lista
print("23.- Remueve el ultimo elemento de la lista  ",companies)

companies.clear()
print(companies)                                                                # 24 .- remueve todos los elementos de la lista []

del companies
print(companies)                                                                # 25 borra complatamente la lista
                                                                                #"NameError: name 'companies' is not defined"



                                            

'''
1. Declare an empty list
2. Declare a list with more than 5 items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, manzana, IBM, Oracle and Amazon.
7. Print the list using _print()_
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print the list after modifying one of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies names to uppercase (IBM excluded!)
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies from the list
25. Destroy the IT companies list
26. Join the following lists:

    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
'''


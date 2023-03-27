
#python
# sintaxis
#if condición:
    #esta parte del código se ejecuta para condiciones verdaderas


#**Ejemplo: 1**

a = 100
if a > 0:
    print('A es un número positivo') # a es un número positivo

### If Else

#Si la condición es verdadera, se ejecutará el primer bloque, si no, se ejecutará la otra condición.

# sintaxis
#if condición:
    #esta parte del código se ejecuta para condiciones verdaderas
#else:
    #esta parte del código se ejecuta para condiciones falsas
    

# Ejemplo 2

a = 5
if a < 6:
    print('a es un número negativo')
else:
    print('a es un número positivo')  #a es un número negativo

### if elif else

#En nuestra vida diaria, tomamos decisiones a diario. Tomamos decisiones no comprobando una o dos condiciones sino múltiples condiciones. Al igual que la vida, la programación también está llena de condiciones. Usamos _elif_ cuando tenemos múltiples condiciones.

# sintaxis
#if condición:
    #código
#elif condición:
    #código
#else:
    #código

# ejemplo 3

a = -10
if a > 0:
    print('A es un número positivo')
elif a < 0:
    print('A es un número negativo')
else:
    print('A es cero')  # a es un número negativo


### condiciones anidadas

#Las condiciones pueden ser anidadas 

# sintaxis
#if condición:
 #   código
 # #if condición:
 #       código

#**Ejemplo: **


a = -10
if a > 0:
    if a % 2 == 0:
        print('a es numero positivo y tambien es entero')
    else:
        print('a es un número positivo')
elif a == 0:
    print('a is zero')
else:
    print('a es un número negativo')  #a es un número negativo

#Podemos evitar escribir una condición anidada usando el operador lógico _and_.
### Condición if y el operador lógico and

# sintaxis
#if condición and condición:
#    código

#*****Ejemplo: ***

a = 13
if a > 0 and a % 2 == 0:
        print('A es un número entero par positivo',a)
elif a > 0 and a % 2 !=  0:
     print('A es un entero',a)
elif a == 0:
    print('A es cero',a)
else:
    print('a  es negativo',a)


### Condición if y el operador lógico or

# sintaxis
#if condición or condición:
#   código

#**Ejemplo: **

usuario = 'admin'
nivel_de_acceso = 3
if usuario == 'admin' or nivel_de_acceso >= 4:
        print('Bienvenido ',usuario)
        print('Acceso concedido!')    #Acceso concedido!
else:
    print('Acceso denegado!',usuario)










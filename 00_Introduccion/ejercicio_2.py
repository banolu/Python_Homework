import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
exp_final=re.findall(patron, frase)
print(exp_final)
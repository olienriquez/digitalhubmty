# Databricks notebook source
'''Asigna un número aleatorio a tu compañero. Los guardarás en un diccionario, junto con el nombre de tu pareja.
Luego imprimirán los valores del diccionario (nombre de la persona y número que dijo) (Usando un bucle for)
 Al final imprimirán dos mensajes, mostrando el número más grande, y el número más pequeño que dijeron, sin el nombre del socio, sólo el número.'''

# COMMAND ----------

import numpy as np
diccionario = {'Gabo':np.random.randn(), 'David':np.random.randn(),'Gaby':np.random.randn()}
for x,y in diccionario.items():
    print(x,':',y)

# COMMAND ----------

minimo = min(list(diccionario.values()))
maximo = max(list(diccionario.values()))
print(f"El número más pequeño fue {minimo} y el más grande fue {maximo}")

# COMMAND ----------

print(f"El número más grande es {}")

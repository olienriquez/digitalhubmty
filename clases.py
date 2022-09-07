# Databricks notebook source
n=[1,2,3]


# COMMAND ----------

import numpy as np

# COMMAND ----------

m = np.array(n)
m.ndim

# COMMAND ----------

m.shape

# COMMAND ----------

lista1 = [1.2, True, "hola",3]
matrizdel1 = np.array(lista1)
matrizdel1
# matrices optimizadas para valores numéricos

# COMMAND ----------

matriz2 = np.array([1,2,3,4,5,6], dtype = "float")
matriz2

# COMMAND ----------

matriz_m = np.array(m)
matriz_n = np.array(n)
matriz_m + matriz_n

# COMMAND ----------

np.maximum(matriz_m,matriz_n), np.minimum(matriz_m,matriz_n)

# COMMAND ----------

vector = np.arange(3,42,1)
prueba = [0,1,2,3,4,0,1,2,3,4]
arreglo = np.array(prueba)
arreglo


# COMMAND ----------

vector

# COMMAND ----------

sorted(arreglo)
np.sort(a)


# COMMAND ----------

arreglo.sort()
arreglo

# COMMAND ----------

bidim = np.array([[18,22,34],[400,300,560]])
bidim

# COMMAND ----------

bidim.shape

# COMMAND ----------

bidim[-1,-1]

# COMMAND ----------

bidim[0,2]


# COMMAND ----------

np.resize(bidim,(10,10))

# COMMAND ----------

f = np.arange(3,31,3)
f

# COMMAND ----------

gg = np.array([f,f])
gg

# COMMAND ----------

h = np.reshape(np.array(range(1,26)),(5,5))
h

# COMMAND ----------

i = np.asarray([1,2,3])
i.dtype

# COMMAND ----------

aux = np.array([1,2,3])
type(aux)

# COMMAND ----------

aux2 = np.asarray([1,2,3])
type(aux2)

# COMMAND ----------

#j = i.astype("complex64")
np.eye(2, dtype = int)

# COMMAND ----------

np.eye(2,3)

# COMMAND ----------

np.eye(2,3,k=1)
# se desplazó hacia la derecha

# COMMAND ----------

np.zeros(3)

# COMMAND ----------

np.ones(shape = (2,3))

# COMMAND ----------

np.empty(shape = (3,3))

# COMMAND ----------

np.identity(4)

# COMMAND ----------

np.full(shape = (2,10), fill_value = False)

# COMMAND ----------

#np.array()
np.reshape(np.array(range(0,9)),(3,3))

# COMMAND ----------

np.eye(6,6)

# COMMAND ----------

# MIERCOLES

# COMMAND ----------



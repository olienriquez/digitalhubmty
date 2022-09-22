# Databricks notebook source
tiempo = float(input("Ingresa tiempo de estancia en minutos: "))


# COMMAND ----------

tiempo = float(input("Ingresa tiempo de estancia en minutos: "))

while tiempo <= 0:
    if tiempo == 0 :
        
        break
    else: 
        tiempo = float(input("Ingresa un tiempo válido:"))

if tiempo > 0 and tiempo <=60:
    tarifa = 25
    print("Total a pagar:",tarifa)


elif tiempo > 60:
    
    if tiempo%60 == 0:
        tarifa = 25 + ((tiempo // 60)-1) * 15
    else:
        tarifa = 25 + ((tiempo // 60)) * 15

    print("Total a pagar:",tarifa)
    


# COMMAND ----------

tiempo


# COMMAND ----------

((tiempo // 60)-1) * 15

# COMMAND ----------



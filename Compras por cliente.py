# Databricks notebook source
# MAGIC %md
# MAGIC Crear un programa que permita al usuario ingresar el tiempo dentro en un estacionamiento , cortando el ingreso de datos cuando el usuario ingresa 0 minutos.
# MAGIC Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar que ingrese una nueva cantidad.
# MAGIC Ingresar una tarifa fija durante la primera hora (60 minutos) de $25 y $15 por cada hora adicional. Al finalizar, informar el total a pagar teniendo en cuenta que, si el monto supera las 8 horas se aplica una tarifa fija de $200 extra.

# COMMAND ----------

tiempo = float(input("Ingresa el tiempo dentro del estacionamiento en minutos:"))

# COMMAND ----------

if tiempo == 0:
    print("Total a pagar: 0")
elif tiempo < 0:
    float(input("Ingresa un tiempo válido:"))
elif tiempo < 60:
    tarifa = 25
    print(f"Total a pagar:{tarifa}")
else:
    if tiempo%60 == 0:
        tarifa = 25 + ((tiempo // 60)-1) * 15
    else:
        tarifa = 25 + ((tiempo // 60)) * 15
        
    print(f"Total a pagar:{tarifa}")
    

# COMMAND ----------



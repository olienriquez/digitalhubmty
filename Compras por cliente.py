# Databricks notebook source
'''Actividad: Avanzada

Crear un programa que permita al usuario ingresar el tiempo dentro en un estacionamiento , cortando el ingreso de datos cuando el usuario ingresa 0 minutos.
Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar que ingrese una nueva cantidad.
Ingresar una tarifa fija durante la primera hora (60 minutos) de $25 y $15 por cada hora adicional. Al finalizar, informar el total a pagar teniendo en cuenta que, si el monto supera las 8 horas se aplica una tarifa fija de $200 extra. '''

# COMMAND ----------

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


elif tiempo > 60 and tiempo < 60*8:
    
    if tiempo%60 == 0:
        tarifa = 25 + ((tiempo // 60)-1) * 15
    else:
        tarifa = 25 + ((tiempo // 60)) * 15

    print("Total a pagar:",tarifa)
else:
    print("Total a pagar:",tarifa + 200)


# COMMAND ----------



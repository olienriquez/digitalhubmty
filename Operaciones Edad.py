# Databricks notebook source
# MAGIC %md
# MAGIC 1.-El doble de mi edad tiene 24 años, ¿cuántos años tengo?

# COMMAND ----------

persona = 24
yo = persona /2 
yo

# COMMAND ----------

# MAGIC %md
# MAGIC 2.- A un tercio de la edad de mi hermana la disminuyo en 15 años. Tengo 6 años. ¿Qué edad tiene?

# COMMAND ----------

 
yo_2 = 6 
hermana = (yo_2 + 15)*3
hermana

# COMMAND ----------

# MAGIC %md
# MAGIC 3.-Determina quién es más grande

# COMMAND ----------

if hermana > yo_2:
    print("Mi hermana es más grande")
else:
    print("Yo soy más grande que mi hermana")

# COMMAND ----------



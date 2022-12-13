# Databricks notebook source
# MAGIC %md # First NoteBook

# COMMAND ----------

#print ('Sivasankar, Hi ')


# COMMAND ----------

# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of tuples of plants data
data = [(1,'siva'),(2,'shreeram'),(3,'revathi')]
header=('ID','Name')

# creating a dataframe
dataframe = spark.createDataFrame(data, header)

# show data frame
dataframe.show()

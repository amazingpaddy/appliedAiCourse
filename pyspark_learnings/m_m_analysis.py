import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import *


def start():
    print("Application starting..")
    spark = SparkSession.builder.appName("PythonMnMCount").getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    data = spark.createDataFrame([("Paddy", 32), ("Uma", 29), ("Harish", 27)], ["Name", "age"])
    print(f"number of Partitions - {data.rdd.getNumPartitions()}")
    data.printSchema()
    data.show()
    data.where(data.age > 28).show()

    # We can define the schema like below.
    schema = StructType([StructField("author", StringType(), False), StructField("title", StringType(), False),
                         StructField("pages", IntegerType(), False)])

    #We can define the schema like below as well
    schema_ddl = "author STRING, title STRING, pages INT"

    new_data = [("Paddy", "Ponniyin Selvan", 1000), ("Gopi", "Sivakamiyin Sabatham", 2000)]
    new_df = spark.createDataFrame(new_data, schema)
    new_df_ddl_schema = spark.createDataFrame(new_data, schema_ddl)
    new_df.show()
    new_df_ddl_schema.show()



if __name__ == "__main__":
    start()

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

def start():
    print("Application starting..")
    spark = SparkSession.builder.appName("PythonMnMCount").getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    data = spark.createDataFrame([("Paddy", 32), ("Uma", 29), ("Harish", 27)], ["Name", "age"])
    print(f"number of Partitions - {data.rdd.getNumPartitions()}")
    data.printSchema()
    data.show()
    data.where(data.age > 28).show()
    data.rdd.map(lambda r: print(type(r)))

if __name__ == "__main__":
    start()
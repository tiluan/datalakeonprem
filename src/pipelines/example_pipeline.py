from pyspark.sql import SparkSession

def process_data(spark):
    # Read data from MinIO
    data = spark.read.format("csv").option("header", "true").load("s3a://my-bucket/data.csv")

    # Perform data processing tasks
    # ...

    # Write processed data back to MinIO
    data.write.format("parquet").mode("overwrite").save("s3a://my-bucket/processed_data.parquet")

if __name__ == "__main__":
    # Create SparkSession
    spark = SparkSession.builder.appName("ExamplePipeline").getOrCreate()

    # Execute the data pipeline
    process_data(spark)

    # Stop SparkSession
    spark.stop()
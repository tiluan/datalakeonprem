# helpers.py

from pyspark.sql import SparkSession

def create_spark_session():
    """
    Create a SparkSession with the necessary configurations.
    """
    spark = SparkSession.builder \
        .appName("DataPipelineProject") \
        .getOrCreate()
    return spark

def read_data_from_minio(spark, bucket, file_path):
    """
    Read data from MinIO using the provided bucket and file path.
    """
    data = spark.read \
        .format("csv") \
        .option("header", "true") \
        .load(f"minio://{bucket}/{file_path}")
    return data

def write_data_to_minio(data, bucket, file_path):
    """
    Write data to MinIO using the provided bucket and file path.
    """
    data.write \
        .format("csv") \
        .option("header", "true") \
        .mode("overwrite") \
        .save(f"minio://{bucket}/{file_path}")
from pyspark.sql import SparkSession
#from pipelines.example_pipeline import ExamplePipeline

def main():
    # Create a SparkSession
    spark = SparkSession.builder \
        .appName("Data Pipeline") \
        .getOrCreate()

    # Initialize the example pipeline
    example_pipeline = ExamplePipeline(spark)

    # Execute the example pipeline
    example_pipeline.execute()

    # Stop the SparkSession
    spark.stop()

if __name__ == "__main__":
    main()
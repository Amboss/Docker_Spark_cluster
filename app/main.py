from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format


def get_spark_session():
    """
    Initiating Spark session
    :return: Spark context
    """
    sql = SparkSession.builder \
        .appName("trip-app") \
        .config("spark.jars", "/opt/spark-app/postgresql-42.2.22.jar") \
        .getOrCreate()
    sc = sql.sparkContext
    return sql, sc


def main():
    """
    Main process
    - connect to DB & creating
    - initiating dataframe (transform csv to sql table)
    - perform filter operation
    :return:
    """
    # Remember, that docker use own network with services names in place of IP
    url = "jdbc:postgresql://db:5432/demo"
    properties = {
        "user": "docker",
        "password": "docker",
        "driver": "org.postgresql.Driver"
    }
    file = "/opt/spark-data/MTA_2014-08-01.csv"
    sql, sc = get_spark_session()

    df = sql.read.load(file, format="csv", inferSchema="true", sep=",", header="true") \
        .withColumn("report_hour", date_format(col("time_received"), "yyyy-MM-dd HH:00:00")) \
        .withColumn("report_date", date_format(col("time_received"), "yyyy-MM-dd"))

    # Filter invalid coordinates
    df.where("latitude <= 90 AND latitude >= -90 AND longitude <= 180 AND longitude >= -180")\
        .where("latitude != 0.000000 OR longitude !=  0.000000 ")\
        .write.jdbc(url=url, table="mta_reports", mode='append', properties=properties)


if __name__ == '__main__':
    main()

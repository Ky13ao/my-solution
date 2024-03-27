from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import count

# địa chỉ ip của mongodb
mongo_host = '172.31.48.1'

spark = SparkSession \
  .builder \
  .master("local[3]") \
  .appName("MyAssessment2") \
  .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1") \
  .config("spark.mongodb.input.uri", f"mongodb://{mongo_host}:27017/ASM2_dev") \
  .config("spark.mongodb.output.uri", f"mongodb://{mongo_host}:27017/ASM2_dev") \
  .getOrCreate()

# cài schema cho collection Answers
answer_schema = StructType([
  StructField("Id", IntegerType()),
  StructField("OwnerUserId", StringType()),
  StructField("CreationDate", StringType()),
  StructField("ClosedDate", StringType()),
  StructField("Score", IntegerType()),
  StructField("ParentId", IntegerType()),
  StructField("Body", StringType())
])

# spark tải dữ liệu từ mongo vào dataframe
answers_df = spark.read \
  .format("mongo") \
  .option("collection", "Answers") \
  .schema(answer_schema) \
  .load()

# nhóm số câu trả lời theo Id của câu hỏi
renamed_answers_df = answers_df.select("ParentId") \
  .withColumnRenamed("ParentId", "Id") \
  .groupBy("Id").agg(count("*").alias("Number of answers"))

# lưu dataframe vào thư mục /tmp/asm2_spark_output cho task mongoimport
renamed_answers_df.write \
  .format('csv') \
  .mode('overwrite') \
  .option("header", "true") \
  .save('/tmp/asm2_spark_output')
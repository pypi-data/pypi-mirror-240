import sys
import datetime, time
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType,FloatType
from pyspark import StorageLevel

def get_data_profile(spark, df, null_cols):
    schema = StructType([ \
        StructField("Column",StringType(),True), \
        StructField("Count",StringType(),True), \
        StructField("NullCount",StringType(),True),\
        StructField("NullPercentage",StringType(),True),\
        StructField("EmptyCount",StringType(),True),\
        StructField("BlankCount",StringType(),True),\
        StructField("MaxLength",IntegerType(),True),\
        StructField("MinLength",IntegerType(),True),\
        StructField("AvgLength",FloatType(),True),\
        StructField("UniqueCount",StringType(),True), \
        StructField("DistinctCount",StringType(),True)
    ])
    emptyRDD = spark.sparkContext.emptyRDD()
    resultdf = spark.createDataFrame(emptyRDD, schema=schema)
    df_count = df.count()
    for x in null_cols:
            if x.upper() in (name.upper() for name in df.columns):
                df=df.withColumn("Length",F.length(F.col(x)))
                df_2=df.agg(F.min(df.Length).alias("MIN"),F.max(df.Length).alias("MAX"),F.avg(df.Length).alias("AVG"))
                df_2.cache()
                Max=df_2.select('MAX').rdd.flatMap(lambda x: x).collect()[0]
                Min=df_2.select('MIN').rdd.flatMap(lambda x: x).collect()[0]
                Avg=df_2.select('AVG').rdd.flatMap(lambda x: x).collect()[0]
                df_distinct_count = df.select(F.col(x)).distinct().count()
                df_unique_count=(df.groupBy(F.col(x)).count()).filter(F.col("count")==1).count()
                df_null_count = df.select(F.col(x)).filter(F.col(x).isNull()).count()
                df_empty_count = df.select(F.col(x)).filter((F.col(x) == '')).count()
                df_blank_count = df.select(F.col(x)).filter((F.col(x) == ' ')).count()
                df_null = spark.createDataFrame([[x,df_count,df_null_count,str(df_null_count*100.0/df_count) + '%' ,df_empty_count,df_blank_count,Max,Min,Avg,df_distinct_count,df_unique_count]],schema=schema)
                resultdf = resultdf.union(df_null)
    schema = StructType([ \
       StructField("ColumnName",StringType(),True), \
       StructField("DataType",StringType(),True)])
    resultdf_dtypes = spark.createDataFrame(df.dtypes, schema=schema)
    FinalDf=resultdf.join(resultdf_dtypes,resultdf.Column==resultdf_dtypes.ColumnName,'inner')
    FinalDf=FinalDf.drop(F.col("ColumnName"))
    df_2.unpersist()
    return FinalDf

from __future__ import print_function
import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("Usage: batch_process  <hdfs_path>", file = sys.stderr)
		exit(-1)
	
	spark = SparkSession.builder.appName("batch_processing").getOrCreate()
	
	
	"""
	#read batch from hdfs 
	11  sys.argv[1]  hdfs://<public DNS>/....
	"""
	
	df = spark.read.json(sys.argv[1])  
	
	df.createOrReplaceTempView("song")
	df.show()
	sqlDF = spark.sql("SELECT groupid as gid, action as action, count(*) as count from song GROUP BY groupid, action ORDER BY count")
	sqlDF.show()
        df.printSchema()
        print("**************************debug*************************")	
	
	sqlDF.write.format("org.apache.spark.sql.cassandra").mode('overwrite')\
		 .options(table = "batch_process", keyspace = "listen").save()


         
	spark.stop()

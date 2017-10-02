import os
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from cassandra.cluster import Cluster
from pyspark.sql import SparkSession

# start this job with:
# spark-submit --master spark://ip-10-0-0-12:7077 --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 stream_process.py 

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'

CASSANDRA_RESOURCE_LOCATION = '../config/cassandra_multi.config'
KAFKA_RESOURCE_LOCATION = '../config/kafka_multi.config'

CASSANDRA_KEYSPACE = 'listen'
CASSANDRA_TABLE = 'batch_result'

# obtain kafka brokers from config
with open(KAFKA_RESOURCE_LOCATION) as f:
        kafka_topic = f.readline().strip()
        kafka_broker = f.readline().strip()
        print ('kakfa topic: '  ,kafka_topic)
        print ('kafka broker: ' ,kafka_broker)

# obtain cassandra hosts from config
with open(CASSANDRA_RESOURCE_LOCATION) as f:
	cassandra_hosts = f.readline().strip()
        print ('cassandra_hosts: ' ,cassandra_hosts)

def sendPartition(iter):
        print ("***********Before everything start**************")
	cassandra_cluster = Cluster([cassandra_hosts])
	cassandra_session = cassandra_cluster.connect(CASSANDRA_KEYSPACE)
        print ("**********************Initial cassandra_cluster***********************")
	for record in iter:
		#sql_statement = "INSERT INTO " + CASSANDRA_TABLE + " (type, event_time, volume) VALUES ('total', \'" + str(record[0]) + "\', " +str(record[1])+ ")"
                sql_statement =  "INSERT INTO " + CASSANDRA_TABLE + " (sond, count, user) VALUES (str(record[0]), str(record[1]), str([record[2]]) )"
                print ("***********setup sql statement**********************")
		cassandra_session.execute(sql_statement)
                print ('****************execute cassandra session**************')
	cassandra_cluster.shutdown()

# Lazily instantiated global instance of SparkSession
def getSparkSessionInstance(sparkConf):
    if ("sparkSessionSingletonInstance" not in globals()):
        globals()["sparkSessionSingletonInstance"] = SparkSession \
            .builder \
            .config(conf=sparkConf) \
            .getOrCreate()
    return globals()["sparkSessionSingletonInstance"]

def DBWrite(rdd):
        #Get the singleton instance of SparkSession
        spark = getSparkSessionInstance(rdd.context.getConf())
        df = spark.read.json(rdd)
        df.createOrReplaceTempView("song")
        df.show()
        sqlDF = spark.sql("SELECT groupid as user, action as song, count(*) as count from song GROUP BY groupid, action ORDER BY count")
        sqlDF.show()
        df.printSchema()
        print("**************************debug*************************")

        sqlDF.write.format("org.apache.spark.sql.cassandra").mode('append')\
                 .options(table = "batch_result", keyspace = "listen").save()


# registering the spark context
conf = SparkConf().setAppName("listen_stream")
sc = SparkContext(conf=conf)

# this is only necessary for manual run and debugging
logger = sc._jvm.org.apache.log4j
logger.LogManager.getLogger("org").setLevel( logger.Level.ERROR )
logger.LogManager.getLogger("akka").setLevel( logger.Level.ERROR )

# registering the streaming context
ssc = StreamingContext(sc, 1)
ssc.checkpoint("hdfs://ec2-35-167-24-116.us-west-2.compute.amazonaws.com:9000/checkpoint/")

# for stateful streaming an initial RDD is required
initialStateRDD = sc.parallelize([])

# dstream from the kafka topic
kafkaStream = KafkaUtils.createDirectStream(ssc, [kafka_topic], {"bootstrap.servers": kafka_broker})

# aggregation on the dstream
lines = kafkaStream.map(lambda x: x[1])
#        .map(lambda x : (x.split(',')[1] + ' ' + str(x.split(',')[2][:5]) + '-0800', int(float(x.split(',')[8])) if x.split(',')[8].replace('.','',1).isdigit() else 0))
#        .reduceByKey(lambda a, b : a + b).updateStateByKey(updateFunc, initialRDD=initialStateRDD)

# sending the results to Cassandra (by partion)
print ("*****************")
lines.foreachRDD(DBWrite)
#lines.foreachRDD(sendPartition)

ssc.start()
ssc.awaitTermination()

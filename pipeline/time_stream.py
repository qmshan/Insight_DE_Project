from  __future__ import print_function
import os
import json
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from cassandra.cluster import Cluster

from datetime import datetime
# start this job with:
# spark-submit --master spark://ip-10-0-0-12:7077 --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 stream_process.py 

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'

CASSANDRA_RESOURCE_LOCATION = '../config/cassandra_multi.config'
KAFKA_RESOURCE_LOCATION = '../config/kafka_multi.config'

CASSANDRA_KEYSPACE = 'listen'
CASSANDRA_TABLE = 'real_time'

# obtain kafka brokers from config
with open(KAFKA_RESOURCE_LOCATION) as f:
        kafka_topic = f.readline().strip()
        kafka_broker = f.readline().strip()
        print ('kakfa topic: '  ,kafka_topic)
        print ('kafka broker: ' ,kafka_broker)

# obtain cassandra hosts from config
with open(CASSANDRA_RESOURCE_LOCATION) as f:
	cassandra_hosts = f.readline()
        print ('cassandra_hosts: ' ,cassandra_hosts)

def sendPartition(iter):
	cassandra_cluster = Cluster([cassandra_hosts])
	cassandra_session = cassandra_cluster.connect(CASSANDRA_KEYSPACE)
	for record in iter.collect():
                #debug print
                #print ("*****************")
                #print(record)
		# cassandra time yyyy-mm-dd HH:mm:ss
		dt = datetime.now()
		time = str(dt)
		"""
		time = str(dt.year) + "-" + str(dt.month) +  "-"\
                	+ str(dt.day) + " " + str(dt.hour) + ":" \
                	+ str(dt.minute) + ":" +  str(dt.second)
		"""
		sql_statement =  "INSERT INTO " + CASSANDRA_TABLE +\
		 " (action,  count, timestamp) VALUES (\'" + str(record["action"]) + "\' ," \
                     +  str(record["count"])  + " , \'" + time  + "\')"
		cassandra_session.execute(sql_statement)
                print ('Write into Canssandra success!')
	cassandra_cluster.shutdown()

# registering the spark context
conf = SparkConf().setAppName("listen_stream")
sc = SparkContext(conf=conf)

# registering the streaming context
ssc = StreamingContext(sc, 5)
ssc.checkpoint("hdfs://ec2-35-167-24-116.us-west-2.compute.amazonaws.com:9000/checkpoint/")

# for stateful streaming an initial RDD is required
#initialStateRDD = sc.parallelize([])

# dstream from the kafka topic
kafkaStream = KafkaUtils.createDirectStream(ssc, [kafka_topic], {"bootstrap.servers": kafka_broker})
"""
{"action": "NextSong", "gender": "M", "user_id": "12332", "ts": "1483229000594", "groupid": 2}

"""
# aggregation on the dstream
lines = kafkaStream.map(lambda (key, value): json.loads(value))
#Lines output: {u'action': u'NextSong', u'gender': u'F', u'user_id': u'11043', u'ts': u'1482666788407', u'groupid': 2}
rdd = lines.map(lambda x : (x["action"] +'_' + str(x["groupid"]), 1)).reduceByKey(lambda a, b : a + b)
#rdd output: (u'NextSong_2', 6184)
#dt = datetime.now()

#time = str(dt.year) + "-" + str(dt.month) +  "-"\
#		+ str(dt.day) + " " + str(dt.hour) + ":" \
#		+ str(dt.minute) + ":" +  str(dt.second)

#rdd = rdd.map(lambda (x): {'userid':x[0].split("_")[0], 'song':x[0].split('_')[1], 'count':str(x[1])})
rdd = rdd.map(lambda (x): {'action':x[0].split("_")[0],    'count':str(x[1])})
#rdd output: {'count': '5732', 'userid': u'NextSong', 'song': u'2'}

#For Debug usage:
rdd.pprint(10)

#lines = kafkaStream.map(lambda x: x[1])
# sending the results to Cassandra (by partion)
#lines.foreachRDD(lambda rdd: rdd.foreachPartition(sendPartition))
rdd.foreachRDD(sendPartition)
ssc.start()
ssc.awaitTermination()

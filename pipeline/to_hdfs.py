from __future__ import print_function
import sys
import time
from kafka import KafkaConsumer
import os
from hdfs3 import HDFileSystem

class Consumer(object):
	def __init__(self, bootstrap_servers, topic):
		"""
		initialize with kafka_server ip and topic
		"""
		self. bootstrap_servers= bootstrap_servers
		self.topic = topic
		self.hdfs_path = '/listened'
        	self.consumer =   KafkaConsumer(bootstrap_servers)
		self.consumer.subscribe([topic])
        	self.block_cnt = 0
        
    	def consume(self,output):
	        """Consumes a stream of listening history from the topic listened.
        	Args:
            	output_dir: string representing the directory to store the 64MB
                before transferring to HDFS
        	Returns:
        	    None
        	"""
		messageBlock = 0
        	timestamp = time.strftime('%Y%m%d%H%M%S')
        	self.temp_file_dir = "%s/%s_%d.dat" % (output, self.topic, messageBlock)
        	self.temp_file = open(self.temp_file_dir,"w")
		
               
        	for message in self.consumer:
                        #print(message)
			
	        	messageBlock += 1
        		self.temp_file.write(message.value + "\n")
        		if messageBlock % 10000==0:
        			if self.temp_file.tell() > 64000000:
        				self.flush_to_hdfs(output)
			
	def flush_to_hdfs(self,dir):
		timestamp = time.strftime('%Y%m%d%H%M%S')
    		self.temp_file.close()
    	
        	hadoop_fullpath = "%s/%s_%s.dat" % (self.hdfs_path, 
                                               self.topic, timestamp)
        	
		self.block_cnt += 1
		os.system("hdfs dfs -put %s %s" % (self.temp_file_dir,hadoop_fullpath))
		os.remove(self.temp_file_dir)


		self.temp_file_dir = "%s/kafka_%s_%s.dat" % (dir,
                                                         self.topic,
                                                         timestamp)
        	self.temp_file = open(self.temp_file_dir, "w")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("Please enter consumer-hdfs <bootstrap_servers>", file=sys.stderr)
		exit(-1)
	#print("consuming.....")	
	cons = Consumer(bootstrap_servers=sys.argv[1], topic = 'listened')
	cons.consume('listened')

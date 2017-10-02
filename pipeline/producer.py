#!/usr/bin/env python
#-*- coding: utf-8 -*- 
from datetime import datetime
from kafka import KafkaProducer
import sys
import time
#from datetime import datetime
import csv
import json
import pandas as pd
import numpy as np

class Producer(object):

	def generator(self, batch_input, bootstrap_servers):
		producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
		file = open(batch_input)
		for line in file:
			message = self.createjson(line)
        		producer.send('listened', message)
            
	def createjson(self, json_line):

		event = json_line.strip()
    		event = event.strip('{}')
    		event = event.split(',\"')

    		ts = event[0].split(":")
    		ts = ts[1].strip("\"")
    		uid = event[1].split(":")
    		uid = uid[1].strip("\"")
		if uid == "":
			groupid = 0
		else:
			groupid = int(uid)/1000000+1

		old_groupid= groupid
    		action = event[3].split(":")
    		action = action[1].strip("\"")
    		if len(event) < 14:
			gender = "U"
		else:
			gender = event[14].split(':')
			gender = gender[1].strip("\"")
  		info = {'ts':ts, 'groupid': groupid, 'user_id': uid, 'action':action, 'gender':gender }
    	
    		info = json.dumps(info, encoding = 'utf-8')
    		#print info
    		return info
		#except:
		#	pass
		
			
if __name__ == "__main__":
	if len(sys.argv) !=3:
		print("Please enter the following arguments: producer bootstrap <path>")
		exit(-1)
		
	producer = Producer()
	while True:
		producer.generator(sys.argv[1], sys.argv[2])

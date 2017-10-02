import datetime
import time
from cassandra.cluster import Cluster


CASSANDRA_IP = ['35.167.24.116']
CASSANDRA_KEYSPACE = 'listen'

cassandra_cluster = Cluster(CASSANDRA_IP)
cassandra_session = cassandra_cluster.connect(CASSANDRA_KEYSPACE)

# continuous querrying of updates
while True:

        """             
        update upgrade
        """
	stmt = "select * from real_time  where action='Upgrade' order by timestamp desc limit 1440"
	
	records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
	
	with open('upgrade.csv', 'w') as f:
		f.write('action,time,count,\n')
		for r in records:
			f.write(r.action + ', ' + r.timestamp + ', ' + str(r.count) + ',\n')
			
	"""		
	update downgrade
	"""
	stmt = "select * from real_time  where action='Downgrade' order by timestamp desc limit 1440"
	records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
	
	with open('downgrade.csv', 'w') as f:
		f.write('action,time,count,\n')
		for r in records:
			f.write(r.action + ', ' + r.timestamp + ', ' + str(r.count) + ',\n')

	
        """             
        update user cancelling
        """

	stmt = "select * from real_time  where action='Cancel' order by timestamp desc limit 1440"
	
	records = cassandra_session.execute(stmt)
	
	with open('cancel.csv', 'w') as f:
		f.write('action,time,count, \n')
		for r in records:
			f.write(r.action + ', ' + r.timestamp + ', ' + str(r.count) + ',\n')

	print 'New update after 5s'
	time.sleep(5)

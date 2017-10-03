import datetime
import time
from cassandra.cluster import Cluster


CASSANDRA_IP = ['35.167.24.116']
CASSANDRA_KEYSPACE = 'listen'

cassandra_cluster = Cluster(CASSANDRA_IP)
cassandra_session = cassandra_cluster.connect(CASSANDRA_KEYSPACE)

# continuous querrying of updates

"""
Batch result updates
"""

"""             
update Upgrade
"""
stmt = "select * from batch_process  where action='Upgrade' order by gid"	
records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
with open('static/results/batch_upgrade.csv', 'w') as f:
	f.write('action,gid,count,\n')
	for r in records:
		f.write(r.action + ', ' + str(r.gid) + ', ' + str(r.count) + ',\n')
			
"""
update Downgrade
"""
stmt = "select * from batch_process  where action='Downgrade' order by gid"
records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
	
with open('static/results/batch_downgrade.csv', 'w') as f:
	f.write('action,gid,count,\n')
	for r in records:
		f.write(r.action + ', ' + str(r.gid) + ', ' + str(r.count) + ',\n')

"""             
update Thumbs Up
"""
stmt = "select * from batch_process  where action='Thumbs Up' order by gid"	
records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
with open('static/results/batch_thumbsup.csv', 'w') as f:
	f.write('action,gid,count,\n')
	for r in records:
		f.write(r.action + ', ' + str(r.gid) + ', ' + str(r.count) + ',\n')
			
"""
update Thumbs Down
"""
stmt = "select * from batch_process  where action='Thumbs Down' order by gid"
records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
	
with open('static/results/batch_thumbsdown.csv', 'w') as f:
	f.write('action,gid,count,\n')
	for r in records:
		f.write(r.action + ', ' + str(r.gid) + ', ' + str(r.count) + ',\n')
		
		

"""
Update Membership Cancellation
"""
stmt = "select * from batch_process  where action='Cancel' order by gid"
records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])

with open('static/results/batch_cancel.csv', 'w') as f:
	f.write('action,gid,count,\n')
	for r in records:
		f.write(r.action + ', ' + str(r.gid) + ', ' + str(r.count) + ',\n')


"""
update realtime results every 5 seconds
"""

while True:

        """             
        update upgrade
        """
	stmt = "select * from real_time  where action='Upgrade' order by timestamp desc limit 1440"
	
	records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
	
	with open('static/results/upgrade.csv', 'w') as f:
		f.write('action,time,count,\n')
		for r in records:
			f.write(r.action + ', ' + r.timestamp + ', ' + str(r.count) + ',\n')
			
	"""		
	update downgrade
	"""
	stmt = "select * from real_time  where action='Downgrade' order by timestamp desc limit 1440"
	records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
	
	with open('static/results/downgrade.csv', 'w') as f:
		f.write('action,time,count,\n')
		for r in records:
			f.write(r.action + ', ' + r.timestamp + ', ' + str(r.count) + ',\n')

	
        """             
        update user cancelling
        """

	stmt = "select * from real_time  where action='Cancel' order by timestamp desc limit 1440"
	
	records = cassandra_session.execute(stmt)
	
	with open('static/results/cancel.csv', 'w') as f:
		f.write('action,time,count, \n')
		for r in records:
			f.write(r.action + ', ' + r.timestamp + ', ' + str(r.count) + ',\n')

	time.sleep(5)

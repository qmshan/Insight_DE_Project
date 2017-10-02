import datetime
import time
from cassandra.cluster import Cluster


CASSANDRA_IP = ['35.167.24.116']
CASSANDRA_KEYSPACE = 'listen'

cassandra_cluster = Cluster(CASSANDRA_IP)
cassandra_session = cassandra_cluster.connect(CASSANDRA_KEYSPACE)

# continuous querrying of updates
#while True:
"""             
update Upgrade
"""
if True:
	stmt = "select * from batch_process  where action='Upgrade' order by gid"
	
	records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
	
	with open('batch_upgrade.csv', 'w') as f:
		f.write('action,gid,count,\n')
		for r in records:
			f.write(r.action + ', ' + str(r.gid) + ', ' + str(r.count) + ',\n')
			
#update Thumbs Down
	stmt = "select * from batch_process  where action='Downgrade' order by gid"
	records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])
	
	with open('batch_downgrade.csv', 'w') as f:
		f.write('action,gid,count,\n')
		for r in records:
			f.write(r.action + ', ' + str(r.gid) + ', ' + str(r.count) + ',\n')





        stmt = "select * from batch_process  where action='Cancel' order by gid"

        records = cassandra_session.execute(stmt)#, parameters=[real_time, Upgrade])

        with open('batch_cancel.csv', 'w') as f:
                f.write('action,gid,count,\n')
                for r in records:
                        f.write(r.action + ', ' + str(r.gid) + ', ' + str(r.count) + ',\n')

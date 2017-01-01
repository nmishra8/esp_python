# We schedule a bunch of jobs coming in queue.
# The algorithm would check if it can put a qos 
# job safely on an existing machine or it needs to spin a new 
# machine.
import random
class job_slice:
	def __init__(self, job_name, job_type, work, qos, deadline):
		self.name     = job_name    # job_name
		self.job      = job_type    # job_type: {qos, batch, low_priority}
		self.work     = work        # work: int
		self.qos      = qos         # qos: decimal between 0-1
		self.deadline = deadline    # deadline: int

# generate a random job queue
def generate_jobqueue(N,qos,app_name):
	job_queue = []
	for i in range(N):
		j_name     = random.choice(app_name)
		j_type     = random.choice(['qos', 'batch', 'low_priority'])
		j_size     = random.choice([100,500,1000])
		j_deadline = random.choice([0.1,0.5,1])
		job = job_slice(j_name, j_type,  j_size, qos, j_deadline);
		job_queue.append(job);
	return job_queue

# read performance data
def loaddata():

def readfile_name():
	with open('../data/All_app.tsv') as f:
    	app_name = f.read().split('\n')
    return app_name

app_name = readfile_name();  
aa = generate_jobqueue(10,0.9,app_name)
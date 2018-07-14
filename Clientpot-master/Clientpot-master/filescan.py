import subprocess
import os
directory='/home/shubham/'
fileobj=open(directory+'/output','a')
for f in os.listdir(directory+'/binaries'):
	p1=subprocess.Popen(['clamscan','-i','-o','--no-summary',directory+'/binaries/'+f],stdout=subprocess.PIPE).communicate()[0]
	if len(p1)>0:
		fileobj.write(p1)

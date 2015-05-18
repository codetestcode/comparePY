
from datetime import datetime
from filecmp import dircmp
import subprocess


remote_diff_path = '/home/ops/gitdrama/'
local_diff_path = 'diff_repo/local_ref/'
remote_dl_folder = "diff_repo/remote_ref/"

username = "ops"
host = "172.16.73.139"



def init_diffs(dmcp,server_name):
	for name in dcmp.diff_files:
		with open('logs/diffs/{}_{}.log'.format(server_name,str(datetime.now())),"w") as diffIO:
			diffIO.write("{} {} {} {} {}\n".format(str(datetime.now()),
				                                 server_name,  name, 
				                                 dcmp.left, dcmp.right))


subprocess.call('scp -r {}@{}:{} {}'.format(username,host, remote_diff_path,
											remote_dl_folder),shell=True)
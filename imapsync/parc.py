#!/usr/bin/env python3
import subprocess

IMAPSYNC = "/usr/local/sbin/imapsync"

file = open("data.txt", "r")
string = file.readline()

def run(cmd, logfile):
    p = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=logfile)
    ret_code = p.wait()
    logfile.flush()

    return ret_code

while string:
    string = file.read().splitlines()
    if not string:
        break
    for line in string:

        fields = line.split(";")
  
        server1 = fields[0]
        user1 = fields[1]
        password1 = fields[2]
        server2 = fields[3]
        user2 = fields[4]
        password2 = fields[5]
     

        cmdstr = IMAPSYNC + " --host1 {0} --user1 {1} --password1 {2} --host2 {3} --user2 {4} --password2 {5} --no-modulesversion".format(server1, user1, password1, server2, user2, password2)
        print(cmdstr)

        file_logs = open("/data/logs.txt", "a")
        result = run(cmdstr, file_logs)
        file_logs.close()
file.close()
print("--- END SYNC ---")
#EOF

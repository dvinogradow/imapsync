#!/usr/bin/python
import subprocess
import time

IMAPSYNC = "/usr/local/sbin/imapsync"

file = open("data.txt","r")
string = file.readline()

while string:
    string = file.read().splitlines()
    if string == '':
        break
    for line in string:

        fields = line.split(";")
  
        server1 = fields[0]
        user1 = fields[1]
        password1 = fields[2]
        server2 = fields[3]
        user2 = fields[4]
        password2 = fields[5]
     
        time.sleep(3)
        
        print(server1 + " " + user1 + " " + password1 + " " + server2 + " " + user2 + " " + password2)

        cmd = [IMAPSYNC, "--host1", "{}".format(server1), "--user1", "{}".format(user1), "--password1", "{}".format(password1), "--host2", "{}".format(server2), "--user2", "{}".format(user2), "--password2", "{}".format(password2), "--no-modulesversion"]
        print(cmd)

        result = subprocess.check_call(cmd)

file.close()
print("--- END SYNC ---"")

import os
import sys
f = open("ExampleLogs.txt",'r')
lignes  = f.readlines()
f.close()
syslogserver = "192.168.2.98"
port = "514"
nbligne = 0
 
for ligne in lignes:
    nbligne+=1  
    os.system("echo \'" +ligne+ "\'|nc -w 1 -u " +syslogserver+" " +port)
    print "Ligne No "+str(nbligne)  
    print ligne

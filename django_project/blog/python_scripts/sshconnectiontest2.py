from paramiko import SSHClient, AutoAddPolicy
#import time
client = SSHClient()
#ssh.load_system_host_keys()
# host key is a cryptographic key used for authenticating computers in the SSH protocol     
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('10.114.10.86', port=22, username='pi', password='raspberry')   #change IP for what is reqd

#time.sleep(5)
#time module causing the ssh connection to remain open. root cause not known. can be used for exploitation when attacking
print('Connected to 10.114.10.86')
stdin, stdout, stderr = client.exec_command("python3 /home/pi/python/conveyor_server.py")
#stdin, stdout, stderr = client.exec_command("ifconfig")
print(f'STDOUT: {stdout.read().decode("utf8")}')

#output=stdout.readlines()
#print(type(output))
#print("\n" .join(output))

stdin.close()
stdout.close()
stderr.close()
client.close()

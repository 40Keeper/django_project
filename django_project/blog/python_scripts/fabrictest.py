#fabric - highlevel implementation of paramiko
#for faster execution speed use Paramiko which contains the primitives
from fabric import Connection
connection=Connection(host="arunkannan@ubuntu", connect_kwargs = {"password" : "askakkd"})
connection.run("python3 /home/arunkannan/Pythonprograms/hello.py")
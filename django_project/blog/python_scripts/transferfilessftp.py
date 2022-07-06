from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()

# host key is a cryptographic key used for authenticating computers in the SSH protocol     
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect('192.168.63.129', port=22, username='arunkannan', password='ksakska')

#open sftp client object
sftp_client=client.open_sftp()

#set remote server path where files are kept
sftp_client.chdir("/home/arunkannan/Pythonprograms")
print("Remote path is", sftp_client.getcwd())

#print(dir(sftp_client))

#downloading file from remote machine

sftp_client.get('hello.py','C:\\Python programs\\file_download_test.py')

#########################################

#uploading file to remote machine

#sftp_client.put('C:\\Python programs\\file_download_test.py','/home/arunkannan/Pythonprograms/file_upload_test.py')



#close sftp client object
sftp_client.close()
client.close()
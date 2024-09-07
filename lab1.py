import paramiko
import time

import paramiko.client

username=input('Username:Kid ')
password=input('Password:Sh185586 ')

for i in range(11,15):
    ip='172.17.10.254'+str(i)
    ssh_client=paramiko.client.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password)
    print('successfully connect to ',ip)
    command=ssh_client.invoke_shell()
    for n in range(10,21):
        print('creating vlan '+str(n))
        command.send('vlan '+str(n)+'\n')
        command.send('q \n')
        command.send('int vlanif '+str(n)+'\n')
        command.send('ip address '+ip+' 24')
        time.sleep(2)
    time.sleep(2)
    output=command.recv(65535)
    print(output.decode('ascii'))
ssh_client.close()

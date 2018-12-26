# -*- coding: UTF-8 -*-
import paramiko
import sys
import threading


# Copy local file to remote server.
def sshclient_scp(hostname, port, username, password, local_path, remote_path):
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)  # 登录远程服务器
    sftp = paramiko.SFTPClient.from_transport(t)  # sftp传输协议
    sftp.put(local_path, remote_path)
    t.close()


def sshclient_scp_get(hostname, port, username, password, remote_path, local_path):
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)  # 登录远程服务器
    sftp = paramiko.SFTPClient.from_transport(t)  # sftp传输协议
    sftp.get(remote_path, local_path)
    t.close()


def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(execmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    line = stdout.read()
    s.close()
    print(hostname + ":")
    print(line)


try:
    file_name = sys.argv[1]
    cmd = sys.argv[2]
except IndexError:
    print('Wrong params!')
    print('Usage :')
    print('       batch.py "$OS_LIST_FILE" "$BATCH_EXECUTE_CMD"')
    print('cat oslist.txt:')
    print('192.168.0.1,22,oracle,passwd1')
    print('192.168.0.2,22,oracle,passwd1')
    print('192.168.0.3,24,oracle,passwd1')
    print('Format is :')
    print('IPADDR,SSHPORT,USERNAME,PASSWORD')
    print('Examples of usage:')
    print('./batch.py "/root/workspace/oslist.txt" "df -h"')

    sys.exit()

# file_name = sys.argv[1]
# cmd= sys.argv[2]

# maintenance_osinfo
with open(file_name) as file_object:
    for line in file_object:
        splits_str = line.rstrip().split(',')
        a = threading.Thread(target=sshclient_execmd,
                             args=(splits_str[0], int(splits_str[1]), splits_str[2], splits_str[3], cmd))
        a.start()
        # print sshclient_execmd(splits_str[0],int(splits_str[1]),splits_str[2],splits_str[3],cmd)
#        print sshclient_scp(splits_str[0], int(splits_str[1]), splits_str[2], splits_str[3], file_name, splits_str[4]+file_name)

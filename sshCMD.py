#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: sshCMD.py 
@time: 2018/11/{DAY} 
描述: 远程shell 命令 默认取服务器的硬件配置

"""

import paramiko


class SSH():
    def __init__(self,ip, port="22",username="root",password="123456"):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

        self.ssh = paramiko.SSHClient()

        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 允许连接不在known_hosts文件上的主机

        self.ssh.connect(hostname=self.ip, port=self.port,
                    username=self.username, password=self.password)
        # ssh连接到服务器

    def sshExec(self,cmdStr):
        stdin, stdout, stderr = self.ssh.exec_command(cmdStr)
        # 执行命令

        out, err = stdout.read(), stderr.read()
        # 执行结果

        result = out if out else err
        # 获取返回信息

        # print(result.decode())
        return result.decode()

    def sshClose(self):
        self.ssh.close()
        # print("ssh client close.")


if __name__=='__main__':
    port,username,password = ["22", "richuser", "richr00t"]
    hostList= [["10.100.162.112","MR1"],
               ["10.100.162.111","MR2"],
               ["10.100.162.110","MR3"],
               ["10.100.162.109","MR4"],
               ["10.100.162.108","MR5"],
               ["10.100.162.115","MR6"],
               ["10.100.162.117","MR7"],
               ["10.100.162.119","MR8"],
               ["10.100.162.120","MR9"]
               ]
    title = "Server  Size  Used  Avail Use%  MountPoint  Proceser  CPU                                  MemTotal MemAvailable"
    cmd = """ echo "`df -h|grep /home | awk '{print $2 "  " $3 "  " $4 "  " $5 "    " $6 "      "}'` `cat /proc/cpuinfo | grep processor |awk 'END {print}' |awk '{print $3+1 }'` `cat /proc/cpuinfo | grep name |awk 'END {print}' |awk '{print "       " $4 " " $5 " " $6 " " $7 " " $10}'` `cat /proc/meminfo | awk '/MemTotal/||/MemAvailable/  {print $2 " "}'|xargs`  " """
    print(title)

    for ip in hostList:
        ssh = SSH(ip[0],port,username,password)
        result = ssh.sshExec(cmd)
        print(ip[1] + "     " + result)
        ssh.sshClose()
















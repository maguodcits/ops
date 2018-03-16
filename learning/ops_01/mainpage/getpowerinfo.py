import paramiko

n =0
# 实例化一个transport对象
trans = paramiko.Transport(('192.168.254.129', 22))
# 建立连接
trans.connect(username='maguo', password='1')
# 将sshclient的对象的transport指定为以上的trans
ssh = paramiko.SSHClient()
ssh._transport = trans
# 执行命令
#输入流，输出流，错误流
stdin, stdout, stderr = ssh.exec_command('df -hl')
for i in stdout:
    i=i.split()
    for a in i:
        n=n+1
        if n>7:
            print(a)
            if (n-7)%6==0:
                print('/n')
# 关闭连接
trans.close()

# coding=utf-8
import paramiko
import base64


def view_log(log_server, cmd):
    server = b'bmV4dXMuMmR1cGF5LmNvbQ=='
    name = b'eWluZ3lpbmc='
    pwd = b'emhheGluYnU2NjY='
    # 连接ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        base64.b64decode(server.decode()),
        username=base64.b64decode(name.decode()),
        password=base64.b64decode(pwd.decode())
    )

    # 建立一个通道
    c = ssh.invoke_shell()

    # 定义一个接收通道返回数据的可变对象
    result = {'data': ''}

    # 发送go，打开跳板列表
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        if result['data'].endswith(']$ ') or result['data'].endswith(']# '):
            # print(result['data'])
            c.send('go\n')
            result['data'] = ''
            break

    # 选择跳板
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        if result['data'].endswith('enter your choice\r\n'):
            # print(result['data'])
            c.send(log_server + '\n')
            result['data'] = ''
            break

    # 发送查看log命令
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        if result['data'].endswith(']$ ') or result['data'].endswith(']# '):
            # print(result['data'])
            c.send(cmd + '\n')
            result['data'] = ''
            break

    # 返回log内容
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        if len(result['data']) > len(cmd)+5:
            # print(result['data'])
            break

    ssh.close()
    return result['data']


if __name__ == "__main__":
    print(view_log('ppcp1o', 'tail -100f /data/log/inspos-dm-ppcp2.log'))

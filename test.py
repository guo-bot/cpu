import socket
import psutil
import yagmail
import time


def ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
def cpu_info():
    cpu = psutil.cpu_percent(1)
    return cpu
res = cpu_info()
def mem_info():
    mem = psutil.virtual_memory()
    info1 = {'mem_total': mem[0], 'mem_free': mem[1], 'mem_percent': mem[2], 'mem_used': mem[3]}
    return info1
res2 = mem_info()
def disk_info():
    disk = psutil.disk_usage(r'c:')
    info2 = {'total': disk[0], 'used': disk[1], 'free': disk[2], 'percent': disk[3]}
    return info2
res3 = disk_info()
def main():
    m_cpu = res
    m_mem = res2
    m_disk = res3
    msg = '''       
            cpu使用率%s%%
            内存总量%sM      
            内存剩余%sM
            内存使用率%s%%
            内存使用量%sM
            磁盘总量%sGB
            磁盘使用量%sGB 
            磁盘剩余量%sGB
            磁盘使用率%s%%
            '''\
    % (m_cpu, int(m_mem.get('mem_total') / 1024 / 1024), int(m_mem['mem_free'] / 1024 / 1024),m_mem['mem_percent'],
    int(m_mem['mem_used'] / 1024 / 1024), int(m_disk['total'] / 1024 / 1024 / 1024),
    int(m_disk['used'] / 1024 / 1024 / 1024),
    int(m_disk['free'] / 1024 / 1024 / 1024), m_disk['percent'])
    print(msg)

    yag = yagmail.SMTP(user='15033350902@163.com', password='WGFGOPFVTLIHTPZV', host='smtp.163.com')
    con=[ip(),msg];
    yag.send(to=['15033350902@163.com','a15033350902@163.com'], subject=ip(), contents=con)
    yag.close()
while True:
    if __name__ == '__main__':
        main()
    time.sleep(180)
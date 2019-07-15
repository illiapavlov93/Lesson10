import time


class Proxy:
    def __init__(self, ip, port, data_used=0, counter=0, user=None, password=None):
        self.ip = ip
        self.port = port
        self.data_used = data_used
        self.counter = counter
        self.user = user
        self.password = password

    def __repr__(self):
        return 'ip: {}, port: {}'.format(self.ip, self.port)

    def __lt__(self, other):
        if self.data_used == other.data_used:
            return False
        elif self.data_used < other.data_used:
            return True


class ProxyManager:
    def __init__(self):
        self.ok = []
        self.banned = []

    def read_from_file(self, f):
        ip_list = []
        file = open(f, encoding='utf-8')
        for line in file:
            ip_list.append(line.strip())
        file.close()
        for i in range(len(ip_list)):
            a = ip_list[i].split(':')
            proxy = Proxy(a[0], a[1])
            self.ok.append(proxy)

    def next_proxy(self):
        if self.ok:
            sort_time = sorted(self.ok)
            proxy = sort_time.pop()
        else:
            return 'no more proxy'
        for i in range(len(self.ok)):
            if self.ok[i] == proxy:
                self.ok.pop(i)
        return proxy

    def back_proxy(self, proxy, status=None):
        proxy.counter += 1
        proxy.data_used = time.time()
        if status == 'ok':
            self.ok.append(proxy)
        elif status == 'banned':
            self.banned.append(proxy)


obj = ProxyManager()
obj.read_from_file('proxies.txt')
obj.back_proxy(obj.next_proxy(), 'ok')
obj.back_proxy(obj.next_proxy(), 'banned')
print(obj.banned)
print(obj.ok)


import requests


def fd(ip, port, **kw):
    resp = requests.get('http://' + ip + ":" + port).json()
    print(resp)


fd("127.0.0.1", "8080", name="Егор")
import threading
from NetComponent.NetServer import NetServer
from NetComponent.NetClient import NetClient
from LogComponent.LogMember import g_main_log

def test_1():
    server = NetServer(10000)
    thread = threading.Thread(target=lambda server: server.Run(), args={server, })
    thread.start()
    input('input any to stop:')
    server.Stop()
    thread.join()
    return

def test_2():
    ip = input('input server ip:')
    client = NetClient(ip, 10000)
    client.Connect()
    g_main_log.info(client.Receive())
    client.Send('hello')
    client.Disconnect()

if __name__ == '__main__':
    test_1()
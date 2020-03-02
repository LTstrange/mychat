import datetime
import socket
import traceback
import uuid
from threading import Thread


class Connection:
    def __init__(self, my_socket: socket.socket, connections: dict):
        self.my_socket = my_socket
        self.connections = connections
        self.data_handler()
        self.undeal_data = []

    def data_handler(self):
        thread = Thread(target=self.recv_data)
        thread.setDaemon(True)
        thread.start()

    def recv_data(self):
        try:
            while True:
                data = self.my_socket.recv(2048)
                if len(data) == 0:
                    self.my_socket.close()
                    self.connections.pop(self)
                    break
                else:
                    msg = data.decode('utf8')
                    msg = msg.split('|#|')
                    self.undeal_data.extend(msg[:-1])
        except ConnectionResetError:
            if self in self.connections:
                self.connections.pop(self)
            Server.write_log('对方断开连接，已强制下线，详细原因：\n' + traceback.format_exc())

        except:
            if self in self.connections:
                self.connections.pop(self)
            Server.write_log('有用户接收数据异常，已强制下线，详细原因：\n' + traceback.format_exc())


class Server:
    __user_cls = None

    @staticmethod
    def write_log(msg: str):
        cur_time = datetime.datetime.now()
        s = '[' + str(cur_time) + ']' + msg
        print(s)

    def __init__(self, ip: str = '127.0.0.1', port: int = 6666):
        self.ip = ip
        self.port = port

        self.connections = {}

        try:
            self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.listener.bind((self.ip, self.port))
            self.listener.listen(5)
        except:
            self.write_log('服务器启动失败，请检查ip端口是否被占用。详细原因：\n' + traceback.format_exc())

        # TODO: 持续监听进程


    def search_connections(self):
        while True:
            client, _ = self.listener.accept()
            client_uuid = uuid.uuid4()
            user = self.__user_cls(client, self.connections)
            self.connections[client_uuid] = {"user": user,
                                             "username": None}
            self.write_log('有新连接进入，当前连接数：{}'.format(len(self.connections)))


if __name__ == '__main__':
    pass

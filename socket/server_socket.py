# 创建TCP服务器
from socketserver import TCPServer, BaseRequestHandler


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg or msg == b'exit\r\n':
                break
            self.request.send(msg)


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()

# 服务器运行后，可以使用telnet来测试它。例如：

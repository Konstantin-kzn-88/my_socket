import socketserver

class ThredingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print(f'Adress: {self.client_address[0]}')
        print(f'Data: {data.decode()}')
        b = bytes('[1,2,3,4]', encoding='utf-8')
        self.request.sendall(b)

if __name__ == '__main__':
    with ThredingTCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
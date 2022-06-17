import socketserver

class ThredingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        def recvall(request):
            BUFF_SIZE = 4096  # 4 KiB
            data = b''
            while True:
                part = request.recv(BUFF_SIZE)
                data += part
                if len(part) < BUFF_SIZE:
                    break
            return data

        full_data = recvall(self.request)
        print(f'Adress: {self.client_address[0]}')
        print(f'Data: {len(full_data)} {full_data}')
        # некая операция
        d = eval(full_data)
        d = d[::-1]

        msg = str(d).encode()
        self.request.sendall(msg)

if __name__ == '__main__':
    with ThredingTCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()
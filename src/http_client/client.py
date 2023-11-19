import socket

class HTTPClient:
    def __init__(self, server, port=80):
        self.server = server
        self.port = port
        self.clientsock = None
        self.connect()

    def connect(self):
        try:
            # socket.AF_INET specifies IPv4 address family
            # socket.SOCK_STREAM specifies TCP socket type
            self.clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientsock.connect((self.server, self.port))
        except socket.error as e:
            print(f"Socket error: {e}")

    def get_website(self, path="/"):
        try:
            # construct HTTP GET request
            # encode() convert string (unicode) into bytes (UTF-8 encoding)
            cmd = f"GET {path} HTTP/1.0\r\n\r\n".encode()
            # send request to the server
            self.clientsock.send(cmd)

            # decode the data
            while True:
                data = self.clientsock.recv(512)
                if len(data) < 1:
                    break
                print(data.decode(), end="")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

    def close(self):
        if self.clientsock:
            self.clientsock.close()

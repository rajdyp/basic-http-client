import socket

def get_website(server, port=80, path="/"):
    try:
        # socket.AF_INET specifies IPv4 address family
        # socket.SOCK_STREAM specifies TCP socket type
        clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsock.connect((server, port))

        # construct HTTP GET request
        # encode() convert string (unicode) into bytes (UTF-8 encoding)
        cmd = f"GET {path} HTTP/1.0\r\n\r\n".encode()
        # send request to the server
        clientsock.send(cmd)

        # decode the data
        while True:
            data = clientsock.recv(512)
            if len(data) < 1:
                break
            print(data.decode(), end="")

    # catch socket-related errors
    except socket.error as e:
        print(f"Socket error: {e}")
    # catch other unexpected errors
    except Exception as e:
        print(f"An unexpected error occured: {e}")

    # close socket in finally block to ensure it's always closed
    finally:
        clientsock.close()

if __name__ == "__main__":
    pass
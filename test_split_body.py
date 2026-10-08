import socket
import time

HOST = "127.0.0.1"
PORT = 8081

request_headers = (
    "POST /upload HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "Content-Length: 11\r\n"
    "\r\n"
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    # Primo recv del server: solo header e parte del body
    sock.sendall(request_headers.encode())
    sock.sendall(b"hello")

    time.sleep(1)

    # Secondo recv del server: resto del body
    sock.sendall(b" world")

    response = b""

    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data

    print(response.decode(errors="replace"))
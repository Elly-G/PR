import socket
import ssl

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("zetcode.com" , 80))
    # ssl.wrap_socket(s.fileno,ssl_version='TLSv1')
    s.sendall(b"GET / HTTP/1.1\r\nHost: zetcode.com\r\nAccept: text/html\r\nConnection: close\r\n\r\n")

    while True:

        data = s.recv(1024)

        if not data:
            break

        print(data.decode())
s.close()        

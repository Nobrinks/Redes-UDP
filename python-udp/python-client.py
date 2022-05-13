import json
import socket

# msgFromClient = 100

msgFromClient = {"type": "int", "val": 100}
bytesToSend = json.dumps(msgFromClient).encode("utf-8")

# bytesToSend = str(msgFromClient).encode('utf8')

serverAddressPort = ("127.0.0.1", 7788)

bufferSize  = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 7788  # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     msgFromClient = {"type": "int", "val": 100}
#     s.connect((HOST, PORT))
#     s.sendall(b"Hello World")
#     data = s.recv(1024)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
# print(f"Received {data!r}")

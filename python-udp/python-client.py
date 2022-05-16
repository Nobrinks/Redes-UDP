import json
import time
import socket

def client_socket():
    """Create a client side socket and return it"""
    return socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def encode_msg(message):
    """Encode the message to utf-8 (bytes)"""
    encoded_msg = json.dumps(message).encode("utf-8")
    return encoded_msg


def send_msg(message: bytes, sock, address_port):
    """Sends the message to the socket server at AddressPort (Address, Port)"""
    sock.sendto(message, address_port)


if __name__ == '__main__':
    SERVER_ADDRESS_PORT = ("127.0.0.1", 7788)
    BUFSIZE = 1024

    while True:
        #encoding msg
        client_msg = encode_msg({"type": "str", "val": "hello"})

        #creating socket
        udp_socket = client_socket()

        #start RTT
        sendTime = time.time()
        send_msg(client_msg, udp_socket, SERVER_ADDRESS_PORT)   #send client's message
        msgFromServer = udp_socket.recvfrom(BUFSIZE)    #receive server's message
        msg = "({:.3f} ms) Message from Server: {}".format((time.time() - sendTime) * 1000, json.loads(msgFromServer[0]))
        print(msg)
        break

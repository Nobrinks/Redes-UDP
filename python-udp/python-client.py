import json
import time
import socket

def client_socket():
    """
    Create a client side socket object and return it
    """
    return socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def encode_msg(message):
    """
    Encode the message to utf-8 (bytes)
    """
    encoded_msg = json.dumps(message).encode("utf-8")
    return encoded_msg


def send_msg(message: bytes, sock, address_port):
    """Sends the message to the socket server at AddressPort (Address, Port)"""
    sock.sendto(message, address_port)


if __name__ == '__main__':
    server_address = "152.92.236.16"
    BUFSIZE = 1024

    while True:

        server_address = input("Digite o endereço IP do servidor (Default 152.92.236.16): ")
        server_port = int(input("Digite a porta desejada (Ex: 99xx - xx = num. chamada): "))
        
        #creating socket
        udp_socket = client_socket()

        input_type = input("Selecione o tipo de mensagem desejada (int | str | char): ")
        try:
            if input_type == "int":
                input_msg = input("Digite o inteiro: ")
            elif input_type == "str":
                input_msg = input("Digite a string: ")
            elif input_type == "char":
                input_msg = input("Digite o caracter: ")
                if len(input_type) != 1:
                    print("Tipo incorreto, digite um caracter.")
                    continue
            #encoding msg
            client_msg = encode_msg({"type": input_type, "val": input_msg})
            #start RTT
            sendTime = time.time()
            send_msg(client_msg, udp_socket, (server_address, server_port))   #send client's message
            msgFromServer = udp_socket.recvfrom(BUFSIZE)    #receive server's message
            msg = "({:.3f} ms) Message from Server: {}".format((time.time() - sendTime) * 1000, msgFromServer[0])
            print(msg)
        except Exception as e:
            print(e)



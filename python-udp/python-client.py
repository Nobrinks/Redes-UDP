import json
import time
import socket

menu_options = {
    1: 'int',
    2: 'char',
    3: 'str',
    4: 'Exit',
}

def print_menu():
    print('Selecione o tipo da mensagem:')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


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


def send_msg(message: bytes, sock):
    """
    Sends the message to the connected socket server
    """
    sock.send(message)


if __name__ == '__main__':
    server_address = "152.92.236.16"
    BUFSIZE = 1024


    while(True):
        server_address = input("Digite o endereço IP do servidor (Default 152.92.236.16): ")
        server_port = int(input("Digite a porta desejada (Ex: 99xx - xx = num. chamada): "))
        #creating socket
        udp_socket = client_socket()
        udp_socket.connect((server_address, server_port))
        print_menu()

        try:
            option = int(input('Digite sua opcao: '))
        except:
            print('Entrada inválida. Por favor, digite um numero ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            input_msg = int(input("Digite o inteiro: "))
        elif option == 2:
            input_msg = input("Digite o caracter: ")
            if len(input_msg) != 1:
                raise Exception
        elif option == 3:
            input_msg = input("Digite a string: ")
        elif option == 4:
            print('Encerrando socket...')
            udp_socket.close()
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

        try:
            client_msg = encode_msg({"type": input_type, "val": input_msg})
            #start RTT
            sendTime = time.time()
            send_msg(client_msg, udp_socket)   #send client's message
            msgFromServer = udp_socket.recvfrom(BUFSIZE)    #receive server's message
            msg = "({:.3f} ms) Message from Server: {}".format((time.time() - sendTime) * 1000, msgFromServer[0])
            print(msg)
        except Exception as e:
            print(e)

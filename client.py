import json
import time
import socket

menu_options = {
    1: 'Enviar int',
    2: 'Enviar char',
    3: 'Enviar str',
    4: 'Mudar endereco ip de destino',
    5: 'Mudar porta de destino',
    6: 'Encerrar programa'
}

def print_menu():
    print('Selecione a opcao desejada:')
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
    DEFAULT_SERVER_ADDRESS = "152.92.236.16"
    DEFAULT_SERVER_PORT = 9929
    BUFSIZE = 1024
    server_address = DEFAULT_SERVER_ADDRESS
    server_port = DEFAULT_SERVER_PORT


    while(True):
        
        # server_address = input("Digite o endereço IP do servidor (Default 152.92.236.16): ")
        # if server_address == '':
        # server_port = int(input("Digite a porta desejada (Ex: 99xx - xx = num. chamada): "))
        print('IP de destino: ', server_address)
        print('Porta: ', server_port)
        #creating socket
        udp_socket = client_socket()
        udp_socket.connect((server_address, server_port))

        print_menu()

        try:
            option = int(input('Digite sua opcao: '))
        except:
            print('Entrada inválida. Por favor, digite um numero ...')

        try:
            #Check what choice was entered and act accordingly
            if option == 1:
                input_msg = int(input("Digite o inteiro: "))
            elif option == 2:
                input_msg = input("Digite o caracter: ")
                if len(input_msg) != 1:
                    raise ValueError('Caracter invalido.')
            elif option == 3:
                input_msg = input("Digite a string: ")
            elif option == 4:
                ip = input("Digite o novo IP (Default 152.92.236.16): ")
                socket.inet_aton(ip)
                server_address = ip if ip else DEFAULT_SERVER_ADDRESS
                continue
            elif option == 5:
                port = int(input("Digite a nova porta: "))
                server_port = port if port else DEFAULT_SERVER_PORT
                continue
            elif option == 6:
                print('Encerrando socket...')
                udp_socket.close()
                exit()
            else:
                print('Opcao invalida. Digite um numero entre 1 e 6.')
        except socket.error:
            print('Endereco IP invalido.')
            continue
        except ValueError:
            print('Digite apenas UM caracter.')
            continue

        try:
            client_msg = encode_msg({"tipo": menu_options[option].split(' ')[-1], "val": input_msg})
            #start RTT
            sendTime = time.time()
            send_msg(client_msg, udp_socket)   #send client's message
            print('\nEsperando resposta do servidor...\n')
            msgFromServer = udp_socket.recvfrom(BUFSIZE)    #receive server's message
            msg = "\n({:.3f} ms) Message from Server: {}\n".format((time.time() - sendTime) * 1000, msgFromServer[0])
            print(msg)
        except Exception as e:
            print(e)

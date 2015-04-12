# -*- coding: utf-8 -*-
from socket import socket

HOST = 'localhost'
PORT = 6031


def main():
    #Crea objeto socket
    s = socket()
    #Abre la conexion con el server
    s.connect((HOST, PORT))
    #Recibe informacion del server
    input_data = s.recv(1024)
    #Imprime la informacion recibida
    print input_data
    while True:
        #Solicita ingreso de caracter
        output_data = raw_input("> ")
        if output_data:
            try:
                #Envia la informacion
                s.send(output_data)
            except TypeError:
                #En caso de dar error por caracteres se hace una convercion
                s.send(bytes(output_data, "utf-8"))
            #Recive mensaje del servidor
            input_data = s.recv(1024)
            #Imprime lo recibido
            print input_data
            #Si lo que enviamos es quit entonces cierra el programa
            if output_data == '\quit':
                return


if __name__ == "__main__":
    main()

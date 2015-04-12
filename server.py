# -*- coding: utf-8 -*-
from socket import socket, error
from threading import Thread
import time


clientes = []


class Client(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """

    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)

        self.conn = conn
        self.addr = addr

    def run(self):
        bienvenido = "\n"*80
        bienvenido += "Bienvenido al server: Saraza"
        self.conn.send(bienvenido)
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024)
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if input_data:
                    if input_data == 'quit':
                        self.conn.close()
                        print(self.addr[0] + " se a desconectado.")
                        clientes.remove(self)
                        print "--%s cliente conectados" % str(len(clientes))
                        break
                    else:
                        self.conn.send("Server: " + input_data)
        self.conn.close()

    def close(self):
        """Método para cerrar el socket."""
        self.conn.close()


def main():
    s = socket()

    # Escuchar peticiones en el puerto 6030.
    print "\n" * 30
    print "=" * 30
    print "Bienvenidos al Server"
    print "=" * 30
    print "Escucando conexiones presione CRT-C para cerrar el proceso."
    s.bind(("localhost", 6031))
    s.listen(2)
    limit_client = 1
    while True:
        try:
            if len(clientes) <= limit_client:
                conn, addr = s.accept()
                print "--%s cliente conectados" % str(len(clientes) + 1)
                print(addr[0] + ":" + str(addr[1]) + " se a conectado.")
                c = Client(conn, addr)
                c.start()
                clientes.append(c)
                print("%s:%d se ha conectado." % addr)
            else:
                conn, addr = s.accept()
                print(addr[0] + ":" + str(addr[1]) + " Intento de conexion rechazado.")
                msg_bienvenido = "\n"*80
                msg_bienvenido += "El server se encuentra completo"
                conn.send(msg_bienvenido)
                conn.close()
        except KeyboardInterrupt:
            for cli in clientes:
                cli.close()
            break

if __name__ == "__main__":
    main()

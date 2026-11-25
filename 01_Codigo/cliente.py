import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("127.0.0.1", 5000))

mensaje = "Hola servidor"

cliente.send(mensaje.encode())

respuesta = cliente.recv(1024)

print("Respuesta del servidor:", respuesta.decode())

cliente.close() 

import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("127.0.0.1", 5000))

servidor.listen()

print("Esperando conexión...")

conexion, direccion = servidor.accept()

print("Cliente conectado")

mensaje = conexion.recv(1024)

print("Mensaje recibido:", mensaje.decode())

respuesta = "Hola cliente, recibí tu mensaje"

conexion.send(respuesta.encode())

conexion.close()
servidor.close()
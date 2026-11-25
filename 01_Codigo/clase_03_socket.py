import socket

servidor = "google.com"
puerto = 443

conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

resultado = conexion.connect_ex((servidor, puerto))

if resultado == 0:
    print("Conexión exitosa")

else:
    print("No se pudo establecer la conexión")

conexion.close()
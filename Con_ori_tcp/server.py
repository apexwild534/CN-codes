import socket
def start_server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', 65432)
	server_socket.bind(server_address)
	server_socket.listen(1)
	print("server listening on", server_address)
	while True:
		print("waiting...")
		connection, client_address = server_socket.accept()
		try:
			print("connected to:", client_address)
			data = connection.recv(1024)
			print(f"received: {data.decode()}")
			if data:
				connection.sendall(data)
				print(f"echoed message: {data.decode()}")
		finally:
			connection.close()
if __name__ == "__main__":
	start_server()

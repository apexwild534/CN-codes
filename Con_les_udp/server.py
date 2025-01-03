import socket
def start_udp_server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_address = ('localhost', 65432)
	server_socket.bind(server_address)
	print("UDP server is listening on", server_address)
	while True:
		print("waiting...")
		data, client_address = server_socket.recvfrom(1024)
		print(f"received: {data.decode()} from {client_address}")
		if data:
			server_socket.sendto(data, client_address)
			print(f"message echoed back to {client_address}")
if __name__ == "__main__":
	start_udp_server()

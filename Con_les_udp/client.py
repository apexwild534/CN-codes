import socket
def start_udp_client():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_address = ('localhost', 65432)
	try:
		message = input("Enter a message to send to the UDP server: ")
		client_socket.sendto(message.encode(), server_address)
		data, server = client_socket.recvfrom(1024)
		print(f"Received echo from server: {data.decode()}")
	finally:
		client_socket.close()
if __name__ == "__main__":
	start_udp_client()

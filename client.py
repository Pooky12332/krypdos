import threading
import socket

def clientHandleMsg(conn: socket.socket):
	while True:
		try:
			msg = conn.recv(1024)

			## If no message, close connection, otherwise, do something
			if msg:
				print(msg.decode())
			else:
				conn.close()
				break

		except Exception as e:
			print(f"[!] Error when handling message: {e}")
			conn.close()
			break

def client():
	ADDR = "172.236.11.73"
	PORT = 8383

	try:
		## Create a socket connection to the server
		clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientSocket.connect((ADDR, PORT))
		## Open a thread that displays messages
		threading.Thread(target=clientHandleMsg, args=[clientSocket]).start()
		print("[+] Connected to server!")

		## Read inputs until a command is sent
		while True:
			msg = input()

			## Quit command - use as example
			if msg == "/quit":
				break

			clientSocket.send(msg.encode())

		clientSocket.close()

	except Exception as e:
		print(f"[!] Error when connecting to server: {e}")
		clientSocket.close()

client()
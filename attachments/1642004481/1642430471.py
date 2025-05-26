import socket

# Simple TCP Server
def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print("Server is listening on port 8080")
    
    conn, addr = server_socket.accept()
    print("Connection from", addr)
    conn.sendall(b'Hello, Client')
    conn.close()

# Simple TCP Client
def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    message = client_socket.recv(1024)
    print("Received from server:", message.decode())
    client_socket.close()

if __name__ == "__main__":
    role = input("Run as (server/client): ").strip().lower()
    if role == 'server':
        tcp_server()
    elif role == 'client':
        tcp_client()
    else:
        print("Invalid role")

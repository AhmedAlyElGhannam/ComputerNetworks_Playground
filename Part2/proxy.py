import socket
import threading

def handle_client(client_socket, remote_host, remote_port):
    request_data = client_socket.recv(4096)
    print("[*] Received request:")
    print(request_data.decode())

    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))
    remote_socket.sendall(request_data)

    while True:
        remote_response = remote_socket.recv(4096)
        if not remote_response:
            break
        client_socket.sendall(remote_response)

    client_socket.close()
    remote_socket.close()

def start_proxy(proxy_host, proxy_port, remote_host, remote_port):
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    proxy_socket.bind((proxy_host, proxy_port))
    proxy_socket.listen(5)

    print(f"[*] Proxy server listening on {proxy_host}:{proxy_port}")

    while True:
        client_socket, addr = proxy_socket.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        proxy_thread = threading.Thread(target=handle_client, args=(client_socket, remote_host, remote_port))
        proxy_thread.start()

if __name__ == "__main__":
    proxy_host = "127.0.0.1"  # Proxy server host
    proxy_port = 8888          # Proxy server port
    remote_host = "www.example.com"  # Remote host to proxy to
    remote_port = 80           # Remote host port

    start_proxy(proxy_host, proxy_port, remote_host, remote_port)

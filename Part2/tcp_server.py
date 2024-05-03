from socket import *

serverPort = 6942
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    
    # Split the request into lines to extract the method and resource
    request_lines = sentence.split('\r\n')
    if len(request_lines) > 0:
        first_line = request_lines[0]
        # Check if the request is a GET request
        if first_line.startswith('GET'):
            print("Received GET request:")
            print(first_line)
            # Display additional request headers if needed
            for line in request_lines[1:]:
                if line:
                    print(line)
    
    # Respond with a simple HTTP/1.1 200 OK response
    response = "HTTP/1.1 200 OK\r\n\r\n"
    connectionSocket.send(response.encode())
    
    connectionSocket.close()

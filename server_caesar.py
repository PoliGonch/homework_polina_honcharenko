import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65433)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
from caesar_code import encrypt_decrypt_data

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            if data:
                temp_string = data.decode('utf-8')
                last_data = encrypt_decrypt_data(temp_string)

                print('sending data back to the client')
                connection.sendall(last_data.encode('utf-8'))
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

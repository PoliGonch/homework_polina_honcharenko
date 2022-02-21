import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
# sock.listen()

while True:
    # Wait for a connection
    print('waiting for a connection')
    data, addr = sock.recvfrom(1024)
    try:
        print('received {!r}'.format(data), 'connection from', addr)

        while True:
            if data:
                print('sending data back to the client')
                sock.sendto(data.upper(), addr)
            else:
                print('no data from', addr)
                break

    finally:
        # Clean up the connection
        sock.close()

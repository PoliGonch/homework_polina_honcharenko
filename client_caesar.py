import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65433  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        choose_action = input('What do you want to do? \n1 - encrypt \n2 - decrypt: \n ')
        if choose_action not in ['1', '2']:
            continue
        elif choose_action == '1':
            action = '+'
        else:
            action = '-'

        input_key = input('Give me a key: \n')
        input_data = input('Give me data: \n')
        string_to_encode = action + '|' + input_key + '|' + input_data

        s.sendall(string_to_encode.encode('utf-8'))
        data = s.recv(1024)
        message = data.decode()

        print('Received', message)

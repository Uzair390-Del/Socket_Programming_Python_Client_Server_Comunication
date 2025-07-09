import socket

host_name=socket.gethostname()
port=5000
#socket object
s_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind((host_name,port))
s_socket.listen(2)
print("Server is listening on {}:{}".format(host_name,port))
# accept connection from the client
conn, address= s_socket.accept()
print("Connection from {}".format(str(address)))

while True:
    recv_data=conn.recv(1024).decode()

    if not recv_data:
        break
    print("From connected user: {}".format(str(address)))

    send_data=input(" -> ")
    conn.send(send_data.encode())
conn.close()
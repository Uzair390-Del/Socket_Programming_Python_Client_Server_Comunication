import socket
# Socket programming is a way to enable communication between two computers (or processes) over a network.

host_name=socket.gethostname()
port=5000

#socket object
c_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#af_inet for ipv4 and sock stream is for tcp conncetion

c_socket.connect((host_name,port))
msg= input(" -> ")
while msg.lower().strip() != 'bye':
    #while sending mesage mesage should be encoded
    c_socket.sendall(msg.encode())
    recv_data= c_socket.recv(1024).decode()
    print("Recieved from server: " + recv_data)
    msg=input("->")
c_socket.close()
    

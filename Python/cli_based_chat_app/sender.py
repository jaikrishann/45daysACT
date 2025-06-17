import socket
try:
    ##creating socket 
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #dgram -- datagram
    print("socket created")
    ip_add = "172.16.1.143"
    port =  8888                                   #0 - 65535
    target_add = (ip_add,port)
    message = input("Enter the message : 😁")
    encoded_msg = message.encode("ascii")
    s.sendto(encoded_msg,target_add)
    print("message sent successfully")
    s.close()

except Exception as e:
    print("An Error occured",e)
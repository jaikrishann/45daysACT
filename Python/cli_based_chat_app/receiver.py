import socket
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("socket created")
    ##sender ke ander ip add receiver ka he aayega 
    # hamesha and receiver ka he aayega khud ka 
    ip_add = "172.16.1.143"
    port  = 8888
    complete_add = (ip_add,port)
    s.bind(complete_add)
    
    while True:
        message , sender_address = s.recvfrom(1024)

        print("Raw Message", message)
        print("Sender Address", sender_address)

        decoded_msg = message.decode("ascii")
        print("Message",decoded_msg)

except Exception as e:
    print("An Error occured",e)
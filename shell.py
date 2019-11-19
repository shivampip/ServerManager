from fabric import Connection
from termcolor import colored 

def rexe(con, cmd):
    try:
        out= con.run(cmd)
        return out.stdout.strip()
    except Exception as e:
        print(color("Error", "red"))
        return "Error: {}".format(e)


def lexe(con, cmd):
    try:
        out= con.local(cmd)
        return out.stdout.strip()
    except Exception as e:
        print(color("Error", "red"))
        return "Error: {}".format(e)



def color(text, col):
    return colored(text, col, attrs= ['bold'])


def cprint(text, col= 'cyan'):
    print(color(text, col))


import os 

def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')


def check_cmd(con, cmd):
    if(cmd in ['stop', 'exit']):
        cprint("Thanks for using", "blue")
        con.close()
        exit()
    elif(cmd=="help"):
        cprint("We are here to help")
        return True 
    elif(cmd in ['cls', 'clear']):
        clear()
        return True 
    return False 


def open_shell(local= False, keys= None):
    host= ""
    con= None
    exe= rexe
    if(local):
        host= "local"
        con= Connection("localhost")
        exe= lexe
        cprint("Welcome to local shell")
    else:
        ip= keys[0]
        port= keys[1]
        user= keys[2]
        password= keys[3]
        host= "{}@{}".format(user, ip)
        con= Connection(ip, port= port, user= user, connect_kwargs= {"password": password})
        exe= rexe
        cprint("Welcome to remote shell")

    path= ""
    while(True):
        cmd= input("{}:{}$ ".format(color(host, "green"), color("~/"+path, "yellow")))
        if(cmd.startswith("cd")):
            cmd= cmd[3:]
            if(cmd== ""):
                continue
            path= "{}{}/".format(path, cmd)
            if(cmd.startswith("..")):
                pd= path.split("/")
                pd= pd[:-3]
                npath= "/".join(pd)
                path= npath+"/"
            continue
        if(check_cmd(con, cmd)):
            continue
        with con.cd(path):
            exe(con, cmd)
    print("Thanks for using")




def get_credentials():
    with open("keyfile.hidden", "r") as f:
        data= f.read()
        return data.split("\n")


if(__name__=="__main__"):
    keys= get_credentials()
    open_shell(keys= keys)
    



    #open_shell(local= True)

from fabric import Connection


def rexe(con, cmd):
    try:
        out= con.run(cmd)
        return out.stdout.strip()
    except Exception as e:
        print("Error while executing command")
        return "Error: {}".format(e)


def lexe(con, cmd):
    try:
        out= con.local(cmd)
        return out.stdout.strip()
    except Exception as e:
        print("Error while executing command")
        return "Error: {}".format(e)

def open_local_shell():
    con= Connection("localhost")
    cmd= "Start"
    while(True):
        cmd= input("$ ")
        if(cmd in ['stop', 'exit']):
            break
        lexe(con, cmd)
    print("Thanks for using local shell")



def open_shell(local= False):
    exe= rexe
    if(local):
        exe= lexe
        print("Welcome to local shell")
    else:
        exe= rexe
        print("Welcome to remote shell")
    con= Connection("localhost")

    path= ""
    while(True):
        cmd= input("{}$ ".format(path))
        if(cmd.startswith("cd")):
            path= "{}{}/".format(path, cmd[3:])
                
        with con.cd(path):
            exe(con, cmd)
    print("Thanks for using")



if(__name__=="__main__"):
    open_shell(local= True)
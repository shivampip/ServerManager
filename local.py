from fabric import Connection


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


open_local_shell()
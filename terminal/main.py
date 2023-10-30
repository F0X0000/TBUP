import subprocess
import os
import terminal
import time
import signal
server = subprocess.Popen(["python3", "server.py"])
username = os.getlogin()
import xmlrpc.client
time.sleep(5)
client = xmlrpc.client.ServerProxy("http://localhost:8000")
client.changedirectory("/home/" + username)

def kill():
    server.kill()
    server.wait()

signal.signal(signal.SIGINT, lambda s, f: kill())

while True:
    try:
        exit = terminal.start()
        if exit == False:
            kill()
            break
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    except ValueError:
        pass

import subprocess
import os
import terminal
import time
server = subprocess.Popen(["python3", "server.py"])
username = os.getlogin()
import xmlrpc.client
time.sleep(5)
client = xmlrpc.client.ServerProxy("http://localhost:8000")
client.changedirectory("/home/" + username)

while True:
    try:
        exit = terminal.start()
        if exit == False:
            server.kill()
            server.wait()
            break
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    except ValueError:
        pass

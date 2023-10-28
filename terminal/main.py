import subprocess
import os
import time
subprocess.Popen(["python3", "server.py"])
username = os.getlogin()
import xmlrpc.client
client = xmlrpc.client.ServerProxy("http://localhost:8000")
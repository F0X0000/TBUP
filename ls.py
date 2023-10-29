import os
import sys
from termcolor import colored
import xmlrpc.client
client = xmlrpc.client.ServerProxy("http://localhost:8000")
q = sys.argv[1]
def ls(path, all=False):
    if os.path.exists(path) and os.path.isdir(path):
        contents = os.listdir(path)
        for item in contents:
            if not all and item.startswith('.'):
                continue
            if os.path.isdir(os.path.join(path, item)):
                print(colored(item, 'blue'))
            else:
                print(item)


path = client.printworkingdirectory()
if q == 'all':
    ls(path, all=True)
else:
    ls(path)
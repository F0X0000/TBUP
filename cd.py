import os
import sys
import xmlrpc.client
client = xmlrpc.client.ServerProxy("http://localhost:8000")
path = client.printworkingdirectory()
q = sys.argv[1]
username = os.getlogin()

def pathcheck(path):
    return os.path.exists(path)

def cd(path, folder):
    if folder == "..":
        segments = path.split("/")
        if len(segments) > 1:
            newpath = "/".join(segments[:-1])
        else:
            newpath = "/"
        return newpath
    elif folder == "0":
        newpath = f"/home/{username}"
        return newpath
    else:
        newpath = os.path.join(path, folder)
        return newpath

newpath = cd(path, q)
if pathcheck(newpath):
    client.changedirectory(newpath)
else:
    print("The system cannot find the directory specified.")
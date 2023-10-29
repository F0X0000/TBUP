import sys
import os
import xmlrpc.client
client = xmlrpc.client.ServerProxy("http://localhost:8000")
path = client.printworkingdirectory()
username = os.getlogin()
q = sys.argv[1]
q2 = sys.argv[2]

description ='''
The create command is a versatile tool that empowers users to generate
new files and folders in their file system. It simplifies the process
of initializing and managing new content, whether it's an empty text
file, a script, or a new directory structure.'''

help ='''
    `file` function is used to create a new empty file with the specified name.
If a file with the same name already exists, it can be overwritten.
    `folder` function is used to create a new directory (folder) with the specified
name. If a folder wisth the same name already exists, a new folder with a unique
name will be generated.'''

if q == "file":
    file = os.path.join(path, q2)
    with open(file, "w") as f:
        pass
elif q == "folder":
    folder = os.path.join(path, q2)
    os.mkdir(folder)
else:
    print(description , help, sep="\n")
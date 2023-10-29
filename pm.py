#  ██▄███▄   ████▄██▄
#  ██▀  ▀██  ██ ██ ██
#  ██    ██  ██ ██ ██
#  ███▄▄██▀  ██ ██ ██
#  ██ ▀▀▀    ▀▀ ▀▀ ▀▀
#  ██
#  ▀▀
# package manager
description = """
A Package Manager (PM) is a software tool that enables users to search, 
manage, and query information about software packages. It facilitates 
the installation, updating, and removal of software packages on a 
computer system or distribution. Package Managers act as intermediaries 
between users and package repositories, making it easier to obtain and 
maintain software. PMs ensure that software dependencies are handled, 
streamlining the process of managing software on a system."""
help = """
    `list' is a command used to display a list of all available packages.
    `install` function, provide a GitHub link as an argument. The function
will download and install the software from the specified GitHub repository.
    The `remove` command uninstalls and deletes software packages from the
system.
"""

import os
import sys
import requests
try:
    a1 = sys.argv[1]
    a2 = sys.argv[2]
    a3 = sys.argv[3]
    a4 = sys.argv[4]
    a5 = sys.argv[5]
    a6 = sys.argv[6]
    a7 = sys.argv[7]
    a8 = sys.argv[8]
    a9 = sys.argv[9]
    a10 = sys.argv[10]
except IndexError:
    pass
username = os.getlogin()
path = os.path.dirname(os.getcwd())
nonpermision = ["pm", "clear", "cd", "ls", "pwd", "create"]
#----------------------------------------------------------------------------#

def lista(directory):
    python_files = [f for f in os.listdir(directory) if f.endswith(".py")]
    return python_files
list = lista(path)
list = [file_name.replace(".py", "") for file_name in list]

def dotgitcheck(folder_name):
    return ".git" in folder_name
def linkgitcheck(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.MissingSchema:
        return False



#----------------------------------------------------------------------------#

if a1 == 'help':
    print(description , help, sep="\n")
elif a1 == 'list':
    for file in list:
        print(file)
elif a1 == 'install':
    if a2 == '0':
        print("pm install <Github link>")
    else:
        if dotgitcheck(a2):
            check = linkgitcheck(a2)
            if check == True:
                os.system("git init {path}")
                os.system(f"git clone {a2} {path}")
                print("Repository cloned successfully.")
            if check == False:
                print("Repository not found at this link.")
        else:
            print("Repository not found at this link.")
elif a1 == 'remove':
    if a2 == '0':
        print("pm remove <package name>")
    else:
        if a2 in nonpermision:
            print(f"You don't have permission to remove {a2}.")
        elif a2 in list:
            os.system(f"rm {path}/{a2}.py")
            os.system(f"rm -rf {path}/{a2}")
            print(f"{a2} removed successfully.")
        else:
            print(f"{a2} not found.")


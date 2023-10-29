import os
import re
import xmlrpc.client
from prompt_toolkit import PromptSession
ps = PromptSession()
client = xmlrpc.client.ServerProxy("http://localhost:8000")
style = ">"
username = os.getlogin()
qw = [" ", " "]
qe = ['', ' ']

def location():
    path = client.printworkingdirectory()
    paths = path.split("/")
    return paths[-1]


def file_exists(file_path):
    return os.path.exists(file_path)
def inp(style):
    i = 0
    q = ps.prompt(style)
    if q == qe:
        q = ' '
        return q
    else:
        q = q.lower()
        list  =  re.findall(r'"[^"]+"|\S+', q)
        list = [re.sub('[\'"]', '', token) for token in list]
        for i in range(50):
            list.extend(['0'])
        return list

def openpy(q, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    path = os.path.dirname(os.getcwd())
    script_path = f"python3 /{path}/{q}.py {q1} {q2} {q3} {q4} {q5} {q6} {q7} {q8} {q9} {q10}"
    if file_exists(f"{path}/{q}.py"):
        os.system(script_path)
    else:
        return True
def start():
    style = f"{location()}>"
    q = inp(style)
    if q[0] == '0':
        return True
    elif q[0] == 'exit':
        return False
    else:
        end = openpy(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10])
        if end == True:
            print(f"'{q[0]}' is not recognized as an internal or external command,operable program or file.")
            return True
        return True
    return True
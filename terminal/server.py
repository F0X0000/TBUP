from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

storage = []

def adddata(name, info):
    global storage
    storage[name] = info
    return True

def getdata(name):
    global storage
    return storage[name]

def deldata(name):
    global storage
    del storage[name]
    return True

directory = None

def changedirectory(newdirectory):
    global directory
    directory = newdirectory
    return True

def printworkingdirectory():
    global directory
    return directory

def runserver():
    server = SimpleXMLRPCServer(("localhost", 8000), logRequests=False)
    server.register_function(changedirectory, "changedirectory")
    server.register_function(printworkingdirectory, "printworkingdirectory")
    server.serve_forever()
try:
    if __name__ == "__main__":
        runserver()
except OSError:
    pass
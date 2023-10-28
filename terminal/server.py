from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


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

if __name__ == "__main__":
    runserver()
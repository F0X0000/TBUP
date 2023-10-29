import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://localhost:8000")

print(client.printworkingdirectory())



clients = "pablo,ricardo,"

def create_client(client_name):
    global clients
    clients+=client_name
    _add_comma()
    
def _add_comma(): 
    global clients
    clients += ","
    

def list_clients():
    global clients
    print(clients)
    
if __name__ == "__main__":
    list_clients()
    create_client("david")
    list_clients()


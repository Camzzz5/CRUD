import sys


clients = ["pablo", "ricardo"]

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input("What is the client\'s name?")
        if client_name == "exit":
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name)
    else: 
        print("Client already exists")
    
    
def delete_client(client_name):
    global clients
    if client_name  in clients:
        clients.remove(client_name)
    else:
        print("Client is not in client's list")   


def search_client(client_name):
    global clients
    for i in clients:
        if i == client_name:
            return True    
    return False 
    
def update_client(client_name, updated_client_name):
    global clients
    if client_name  in clients:
        index = clients.index(client_name)
        clients[index]=  updated_client_name
    else:
        print("Client is not in client's list")

def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print(f"{idx} : {client}")
    
    
def _print_welcome():
    print("Welcome to Ventas")
    print("*"*50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[L]ist clients")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch clients")
    
if __name__ == "__main__":
    _print_welcome()
    
    command = input().upper()
    
    if command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == "L":
        list_clients()
    elif command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == "S":
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print("The client is in the client\'s list ")
        else:
            print(f"The client {client_name} is not in the client\'s list ")
            
    elif command == "U":
        client_name = _get_client_name()
        updated_client_name = input("What is the updated client's name?")
        update_client(client_name, updated_client_name)
        list_clients()
    else:
        print("Invalid command")
    



import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Sofware Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
]


def _get_client_field(field_name):
    field = None
    
    while not field:
        field = input(f"What is the client {field_name}?")
    
    return field
    
    
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

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else: 
        print("Client already exists")
    
    
def delete_client(client_name):
    global clients
    indice = search_client(client_name)
    if indice != None:
        del clients[indice]
    else:
        print("Client is not in client's list")   

def _get_client_from_user():
    client_updated = {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Sofware Engineer'  
    }
    return client_updated


def search_client(client_name):
    global clients
    for i in clients:
        if i["name"]  == client_name:
            return True
    return False 
    
def update_client(id, updated_client):
    global clients
    if id <= len(clients) and id >= 0:
        clients[id] = updated_client
    else:
        print("Client is not in client's list")

def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']))
    
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
        client = _get_client_from_user()
        clients.append(client)
        list_clients()
    elif command == "L":
        list_clients()
    elif command == "D":
        delete_client(_get_client_field("name"))
        list_clients()
    elif command == "S":
        
        client_name = _get_client_field("name")
        found = search_client(client_name)
        if found:
            print("The client is in the client\'s list ")
        else:
            print(f"The client {client_name} is not in the client\'s list ")
            
    elif command == "U":
        
        id = update_client(_get_client_field("id"))    
        updated_client =  _get_client_from_user()   
        list_clients()
    else:
        print("Invalid command")
    



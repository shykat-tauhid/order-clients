import json

def read_json(f:str)->list:
    with open(f, 'r') as file:
        data = json.load(file)
    return data

def order_by_priority(json_list:list)->list:
    return sorted(json_list, key=lambda x: x['priorita'], reverse=True)

def add_new_client(new:dict, data:list[dict])->list:
    data.append(new)
    return order_by_priority(data)

def get_highest_heritage(l:list[dict])->dict:
    return sorted(l, key=lambda x: x['patrimonio'])[-1]

def add_id(data:list[dict]):
    id = 0
    for elem in data:
        elem['id'] = id
        id += 1
    return data

def sell(data:list[dict], value:float, client_id:int):
    for client in data:
        if client["id"] == client_id:
            client["patrimonio"] = client["patrimonio"] - value


def main():
    data = read_json('clienti.json')
    data = add_id(data)
    new_client = {
        "nome": "Luca",
        "cognome": "Rossi",
        "eta": 100,
        "patrimonio": 840133.69,
        "priorita": 6,
        "id": 100
    }
    sell(data, 1000000, 0)
    ordered = add_new_client(new_client, data)

    for row in ordered:
        print(row)
    
    print('\n')
    print(f"Richest: ", get_highest_heritage(data))


if __name__ == "__main__":
    main()
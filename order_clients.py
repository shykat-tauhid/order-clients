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

def add_id(data:list[dict])->list:
    id = 0
    for elem in data:
        elem['id'] = id
        id += 1
    return data

def sell(data:list[dict], value:float, client_id:int)->None:
    for client in data:
        if client["id"] == client_id:
            client["patrimonio"] = client["patrimonio"] - value

def age(data:list[dict])->dict:
    ages = {
        "<18": [],
        "18-29": [],
        "30-39": [],
        "40-59": [],
        "60+": []
    }

    for elem in data:
        val = elem["eta"]
        if val < 18:
            ages["<18"].append(elem)
        elif 18 <= val <= 29:
            ages["18-29"].append(elem)
        elif 30 <= val <= 39:
            ages["30-39"].append(elem)
        elif 40 <= val <= 59:
            ages["40-59"].append(elem)
        else:
            ages["60+"].append(elem)
    return ages


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

    age_groups = age(data)
    for group, clients in age_groups.items():
        print(f"{group}: {clients}")
        print('\n\n')

if __name__ == "__main__":
    main()
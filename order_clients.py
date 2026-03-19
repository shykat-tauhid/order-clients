import json

def read_json(f:str)->list:
    with open(f, 'r') as file:
        data = json.load(file)
    return data

def order_by_priority(json_list:list)->list:
    return sorted(json_list, key=lambda x: x['priorita'], reverse=True)

def main():
    data = read_json('clienti.json')
    ordered = order_by_priority(data)

    for row in ordered:
        print(row)


if __name__ == "__main__":
    main()
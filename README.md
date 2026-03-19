# Order Clients Manager

A program to manage and process client data stored in JSON format. This application allows to read client records, sort them by priority, add new entries, and identify high-value clients based on their heritage.

## Features

- **JSON Data Integration**:  Reads client data from local JSON files.
- **Priority Sorting**: Automatically orders the client list based on their assigned priority (from highest to lowest).
- **Client Management**: Add new client records to the existing database while maintaining the sorted order.
- **Financial Analytics**: Identify the "Richest" client based on their heritage (patrimonio).

## Project Structure

- [order_clients.py](C:\Users\shyka\OneDrive\Desktop\python\lezioni_school\Clienti-Git\order_clients.py): The main Python script containing the logic for data processing.
- [clienti.json](C:\Users\shyka\OneDrive\Desktop\python\lezioni_school\Clienti-Git\clienti.json): (Ignored by Git) The data source containing client information in JSON format.
- [.gitignore](C:\Users\shyka\OneDrive\Desktop\python\lezioni_school\Clienti-Git\.gitignore): Configured to ignore the clients dataset.

## Methods

### read_json(file_path: str) -> list
Opens and parses a JSON file, returning its content as a Python list.

```python
def read_json(f:str)->list:
    with open(f, 'r') as file:
        data = json.load(file)
    return data
```

### order_by_priority(json_list: list) -> list
Returns a new list of clients sorted by `priorita` in descending order.

```python
def order_by_priority(json_list:list)->list:
    return sorted(json_list, key=lambda x: x['priorita'], reverse=True)
```

### add_new_client(new_client: dict, data: list) -> list
Appends a new client dictionary to the data list and returns the updated, sorted list.

```python
def add_new_client(new:dict, data:list[dict])->list:
    data.append(new)
    return order_by_priority(data)
```
### get_highest_heritage(client_list: list) -> dict
Analyzes the list to find and return the client record with the highest `patrimonio` value.

```python
def get_highest_heritage(l:list[dict])->dict:
    return sorted(l, key=lambda x: x['patrimonio'])[-1]
```
### add_id() -> list
Adds a new key-value pair for each client containing a unique int key

```python
def add_id(data:list[dict])->list:
    id = 0
    for elem in data:
        elem['id'] = id
        id += 1
    return data
```

### sell(data:list[dict], value:float, client_id:int) -> None
Takes the unique client id, the client list and a price, substracts the `value` to the `patrimonio` of the client

```python
def sell(data:list[dict], value:float, client_id:int)->None:
    for client in data:
        if client["id"] == client_id:
            client["patrimonio"] = client["patrimonio"] - value
```

### def age(data:list[dict]) -> dict
categorize the clients based on the age

```python
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
```
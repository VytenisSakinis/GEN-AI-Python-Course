import requests
 
def get_jsonplaceholder_data(endpoint="todos"):
    url = f"https://jsonplaceholder.typicode.com/{endpoint}"
    response = requests.get(url)
   
    if response.status_code == 200:
        todos = response.json()
        first_10_todos = todos[:10]
        for todo in first_10_todos:
            print(todo)
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}

    
get_jsonplaceholder_data("todos")

print("_________________________")

def get_jsonplaceholder_lastdata(endpoint="todos"):
    url = f"https://jsonplaceholder.typicode.com/{endpoint}"
    response = requests.get(url)
   
    if response.status_code == 200:
        todos = response.json()
        first_10_todos = todos[-10:]
        for todo in first_10_todos:
            print(todo)
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}

    
get_jsonplaceholder_lastdata("todos")
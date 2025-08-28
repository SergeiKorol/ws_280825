import requests

def create_test():
    body = {"title": "run", "completed": True}
    response = requests.post("https://sky-todo-list.herokuapp.com/", json=body)
    response_body = response.json()

    assert response.status_code == 202
    assert response_body['completed'] == True


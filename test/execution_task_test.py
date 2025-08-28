import requests

def test_add():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response_body["id"]

    assert response.status_code == 202
    assert response_body['completed'] == False

    body = {"completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    response_body = response.json()

    assert response_body['completed'] == True
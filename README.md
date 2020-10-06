# Django-Rest-Api-Example

### Развертывание
На данный момент данный сервис не лежит на каком-хостинге, поэтому его нужно поднимать локально.
Требуемые пакеты находятся в requirements.txt

### Как пользоваться
#### Get
1. Для получеия данных о всех пользователях воспользуйтесь:
requests.get('http://127.0.0.1:8000/api/users/').json()
2. Для получения данных об одном пользователе воспользуйтесь:
requests.get('http://127.0.0.1:8000/api/users/<user_id>').json()
#### Post
1. Для добавления нового пользователя воспользуйтесь:
requests.post('http://127.0.0.1:8000/api/users/', json=data).json(), 
где data = {'name': 'name', 'role': 'role'}
#### Put
1. Для изменения данных о пользователе воспользуйтесь:
requests.put('http://127.0.0.1:8000/api/users/<user_id>', json=data).json(), 
где data = {'name': 'name', 'role': 'role'}
#### Delete
1. Для удаления пользователя воспользуйтесь:
print(requests.get('http://127.0.0.1:8000/api/users/<user_id>').json()), 
где <user_id> - идентификатор пользователя


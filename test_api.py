from pprint import pprint
from requests import get, post, delete, put

import logging

logging.basicConfig(level=logging.DEBUG)


# pprint(get('http://localhost:8080/api/jobs').json())
# pprint(get('http://localhost:8080/api/jobs/1').json())
# pprint(get('http://localhost:8080/api/jobs/77').json())
# pprint(get('http://localhost:8080/api/jobs/qq').json())


# print(post('http://localhost:8080/api/jobs', json={}).json())
#
# print(post('http://localhost:8080/api/jobs',
#            json={'job': 'Название работы'}).json())

# print(post('http://localhost:8080/api/jobs',
#            json={'job': 'Название работы добавленное из API',
#                  'work_size': 24,
#                  'team_leader': 1,
#                  'collaborators': "2,3"}
#            ).json())

# print(delete('http://localhost:8080/api/jobs/4').json())
# print(delete('http://localhost:8080/api/jobs/99').json())
# print(delete('http://localhost:8080/api/jobs/qqq').json())

#
# print(post('http://localhost:8080/api/jobs/4',
#            json={'job': 'Измененное название работы через API',
#                  'work_size': 99}).json())


# pprint(get('http://localhost:8080/api/v2/users').json())
# pprint(get('http://localhost:8080/api/v2/users/1').json())
# pprint(get('http://localhost:8080/api/v2/users/1999').json())
# pprint(get('http://localhost:8080/api/v2/users/dffg').json())


# print(post('http://localhost:8080/api/v2/users',
#            json={'surname': 'Ivanova',
#                  'name': 'Clara',
#                  'age': 24,
#                  'position': "worker",
#                  'speciality': "doctor",
#                  'address': "Mars",
#                  'email': "qq@qq",
#                  'password': "123",
#                  }
#            ).json())

# print(delete('http://localhost:8080/api/v2/users/6').json())
# print(delete('http://localhost:8080/api/v2/users/199').json())
# print(delete('http://localhost:8080/api/v2/users/www').json())



# pprint(get('http://localhost:8080/api/v2/jobs').json())
# pprint(get('http://localhost:8080/api/v2/jobs/1').json())
# pprint(get('http://localhost:8080/api/v2/jobs/77').json())
# pprint(get('http://localhost:8080/api/v2/jobs/qq').json())


# print(post('http://localhost:8080/api/v2/jobs', json={}).json())
#
# print(post('http://localhost:8080/api/v2/jobs',
#            json={'job': 'Название работы'}).json())

print(post('http://localhost:8080/api/v2/jobs',
           json={'job': 'Название работы добавленное из API v2',
                 'work_size': 8,
                 'team_leader': 3,
                 'collaborators': "2,4"}
           ).json())
#
# print(delete('http://localhost:8080/api/v2/jobs/6').json())
# print(delete('http://localhost:8080/api/v2/jobs/99').json())
# print(delete('http://localhost:8080/api/v2/jobs/qqq').json())


print(post('http://localhost:8080/api/v2/jobs/5',
           json={'job': 'Измененное название работы через API V2',
                 'work_size': 6}).json())

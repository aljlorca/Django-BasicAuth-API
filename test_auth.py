"""

This script test the API, it returns the user created in SQLite

"""

import requests
from requests.auth import HTTPBasicAuth



basic = HTTPBasicAuth('test', 'hola1133')


r = requests.post('http://127.0.0.1:8000/API/test/', auth=basic)


print(r.content)
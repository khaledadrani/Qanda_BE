import requests 

resp = requests.get('http://localhost:8000/qa')

print('result ',resp.status_code)

print(resp.json())
import requests

print(requests.post('http://127.0.0.1:5000/timer/update', json={'time': 1.1*60}))

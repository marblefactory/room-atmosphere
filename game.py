import requests

print(requests.post('http://pi:5000/timer/update', json={'time': 62}))

import requests

# print(requests.post('http://pi:5000/timer/update/300'))
#print(requests.post('http://192.168.0.32:5000/timer/update/300'))
# print(requests.post('http://192.168.0.32:5000/timer/update/10'))
print(requests.post('https://192.168.0.32/terminals/0', verify=False))

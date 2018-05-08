import requests

# print(requests.post('http://pi:5000/timer/update/5'))
print(requests.post('https://192.168.1.3/terminals/0', verify=False))
#

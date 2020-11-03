import requests

url = 'http://localhost:5050/predict'
r = requests.post(url,json={'message': "You have won a 1 month FREE membership for our $80,000 Prize Jackpot! Reply with : Received"})

print(r.content)
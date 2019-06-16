import requests
import json

userId = "3F628CB7-F0C5-4F56-A720-3F5BBD44C2EA"
r = requests.get(f'http://localhost:10000/api/actions/{userId}/simple')
data = r.json()
print(data['firstName'])
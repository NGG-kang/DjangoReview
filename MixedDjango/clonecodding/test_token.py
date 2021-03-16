import requests

JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImthbmciLCJleHAiOjE2MTU4OTU4OTgsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE2MTU4OTU1OTh9.tXGT-0pvML5ADkUAQj8E1meU_N11SDcwbddzlJW535E'
headers = {
    'Authorization': f'JWT {JWT_TOKEN}',
}
res = requests.get("http://localhost:8000/instagram/post/1", headers=headers)
print(res.json())
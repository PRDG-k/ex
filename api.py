import requests

url = "https://api.sampleapis.com/avatar/info"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print("API 데이터:", data)
    # for i in data:
    #     print(f"ID: {i['id']}, 제목: {i['synopsis']}")
else:
    print("실패", response.status_code)
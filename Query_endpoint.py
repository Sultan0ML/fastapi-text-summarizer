import requests

def qry(text):
  url = "http://0.0.0.0:8080/query"  # Replace with your API URL
  headers = {"Content-Type": "application/json"}


  data={
    "query": text
  }

  response = requests.post(url, json=data, headers=headers)

  # print(response.status_code)
  # print(response.json())
  return response.json()
import requests
def summary(text):
    url = "http://0.0.0.0:8080/summarize"  # Replace with your API URL
    headers = {"Content-Type": "application/json"}
    data = {
        "text": text
    }

    response = requests.post(url, json=data, headers=headers)

    # print(response.status_code)
    # print(response.json())
    return response.json()
import json

import requests

def print_response(response):
  print(response.status_code)
  if 'application/json' in response.headers['Content-Type']:
    print(response.json())
  else:
    print(response.text)

url = "https://petstore.swagger.io/v2/pet"

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

payload_post = json.dumps({
  "name": "test_cat",
  "status": "available"
})

response_post = requests.post(url, headers=headers, data=payload_post)
print_response(response_post)

id = response_post.json()['id']

payload_put = json.dumps({
  "id": id,
  "name": "Малыш"
})

response_put = requests.put(url, headers=headers, data=payload_put)
print_response(response_put)

response_get = requests.get(url + '/findByStatus', headers=headers, params={'status': 'available'})
print_response(response_get)

response_delete = requests.delete(url + '/' + str(id))
print_response(response_delete)

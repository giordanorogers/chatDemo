import requests
import json
url = "https://us-east-1.aws.data.mongodb-api.com/app/data-yuynu/endpoint/data/v1/action/findOne"
payload = json.dumps({
    "collection": "<COLLECTION_NAME>",
    "database": "<DATABASE_NAME>",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'q50gTFSgcBNaqbVQUYp3K9GskI8dbLz5KXm979mzaTbnsX4x2rVEC5OocHvk2PF2',
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)


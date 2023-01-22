import requests
import json


articleindex = 1;

url = "http://localhost:1337/api/blogs/"+str(articleindex)

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)

x = json.loads(response.text);
# print(x['data'][index]['attributes']['AuthorID']);
if x["data"] is None:
    print("error 1 in first URL")
else:
    authorId = x['data']['attributes']['AuthorID']
    print(authorId)
    url2 = "http://localhost:1337/api/authors/"+str(authorId);
    response2 = requests.request("GET", url2, headers=headers, data=payload)

    print(response2.text)


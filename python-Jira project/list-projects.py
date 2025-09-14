# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://yadneshmraut.atlassian.net//rest/api/3/project"

API_TOKEN= "ATATT3xFfGF0hp0AwLFTAC00ecL5otRINV-Gf9mdrYfKS5ujF66V4DjGNtKU09PnXdd_H-qUHEHs9x3LE95AW26B3jXc_FcX6ha7tgDqFDIgXZ4KLs5BCU5iraunN1OvUx0Pw5lWKQxQdAD5nFENmSpekyInroZEzEYtXZ5M_7hMlsjmEgiqFcI=99A35E5E"

auth = HTTPBasicAuth("yadneshmraut@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
for item in output:

    name= item ["name"]

    print(name)

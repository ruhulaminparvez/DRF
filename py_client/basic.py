import requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"Hello World!"}) #HTTP REQUEST
print(get_response.text) #Print Raw Text Response

# HTTP REQUEST -->  HTML 
# REST API (HTTP REQUEST) -->  JSON(xml)


# JavaScript Object Notation (JSON) ~> Python Dictionary

# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.27.1",
#     "X-Amzn-Trace-Id": "Root=1-62207838-26683b8e7b345afb0fc9066e"
#   },
#   "json": null,
#   "method": "GET",
#   "origin": "59.153.103.28",
#   "url": "https://httpbin.org/anything"
# }

print(get_response.json()) #Print JSON Response

# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.27.1', 'X-Amzn-Trace-Id': 'Root=1-62207c75-403e19450ca58aa01cfba52f'}, 'json': None, 'method': 'GET', 'origin': '59.153.103.28', 'url': 'https://httpbin.org/anything'}


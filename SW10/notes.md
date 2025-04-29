# Web services

## Distributed applications

Parts of the application are distributed across multiple computers on the Internet, such as:
WWW, email, YouTube, E-Banking, Whatsapp, Massive Multiplayer Online Games (MMOGs)

Web services follow the client-server model:

- Server application provides services for clients;
- Client consumes services over the Internet by contacting the server;
- Client sends a request, the server sends a response;

## Addressing

Addressing in the Internet is generally done using IP address and port number:

- **IP address**: identifies a host connected to the network (eg. ```147.88.201.68```)
- **Port number**: identifies a process (like a running programm) on a host (eg. ```80``` for HTTP, ```443``` for HTTPS, ```25``` for SMTP, etc.)
- **Hostname**: name of a host. It can be used instead of the IP address (eg. ```www.google.com```)

## Application protocols
In order for the distributed parts of an application to understand each other, they must
speak a common language and agree on rules. This is called an application protocol.

Among others, the following agreements must be made:
- **Addressing the service**: which specific (sub)service do I want to use?
- **Data rappresentation**: how are data (request, response) transmitted?
- **Error messages**: how are error states encoded?

### HTTP requests in Python
```python
import requests

URL = "http://www.w3schools.com/python/demopage.htm"

response = requests.get(URL)

print( "Status Code :", response.status_code) # 200 Ok
print( "Content-Type :", response.headers["Content-Type"] ) # text/html
print( "Response BODY\n", response.text ) # HTML document

# see example in ./REST_examples/web-request.py
```

## REST - REpresentational State Transfer
REST is a software architecture style for developing web apps/services.
- REST is not a standard:
  - Concrete implementations can conform to REST more or less;
  - But by now it’s an ”industry standard” / best practice;
- ... ...

### REST request
REST request to query the position of the International Space Station (ISS) in Python:
```python
import requests

URL = "http://api.open-notify.org/iss-now.json"
rsp = requests.get(URL)

print("Status Code :", rsp.status_code) # 200 Ok
print("Content-Type:", rsp.headers["Content-Type"]) #application/json
print("Response BODY as JSON\n", rsp.json()) # JSON-encoded data

# see example in ./REST_examples/REST-request.py
```

## JSONs - Javascript Object Notation
JSON (vs. Python Dictionary):
- Transmitted and stored as strings – internal representation of a Python dictionary is
not visible to the programmer
- Name of the name-value pair always a string in JSON – can be any object in Python

### Parse JSON
```python
response = requests.get(URL)
response_dict = response.json() # create dict from JSON
value = response_dict.get("key") # value for name ’key’
```

### Create JSON
```python
jsonify( {"users": user_list} ) # creates JSON from user_list
```

... ... ... ...
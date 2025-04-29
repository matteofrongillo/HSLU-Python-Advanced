import requests

URL = "http://www.w3schools.com/python/demopage.htm"

response = requests.get(URL)
print( "Status Code  :", response.status_code)

if not response.ok:
        print( "ERROR" )
else:
    print( "Content-Type :", response.headers["Content-Type"] ) 
    print( "Response BODY as text:\n", response.text )
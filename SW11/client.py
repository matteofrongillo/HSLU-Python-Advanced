import requests

URL = "http://127.0.0.1:5000/api/board" # change if required

response = requests.get(URL)

if not response.ok:
    print("Status-Code: ", response.status_code)
else:
    print( "Response as JSON: \n", response.json() ) # JSON as dict
    print( "entire board: ", response.json()["board"] ) # board as list of list
    print( "row 1: ", response.json()["board"][1] ) # just one row
    print( "token at (1,0):", response.json()["board"][1][0]) # just one token
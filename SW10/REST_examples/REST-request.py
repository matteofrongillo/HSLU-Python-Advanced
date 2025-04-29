import requests

URL = "http://api.open-notify.org/iss-now.json"

response = requests.get(URL)
print( "Status Code  :", response.status_code)

if not response.ok:
    print( "ERROR" )
else:
    print( "Content-Type :", response.headers["Content-Type"] ) 
    rsp_dict = response.json() # entire JSON response as dictionary 
    print( rsp_dict ) 
    pos = rsp_dict["iss_position"] # "iss_position" as dictionary
    print( f"ISS is at position: lat {pos['latitude']}, long {pos['longitude']}.")

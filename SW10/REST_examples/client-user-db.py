import requests

# RASPI_HOSTNAME = "eee-w014-007.simple.eee.intern" # your Raspi-hostname here!
RASPI_HOSTNAME = "localhost"

PORT="5000"
BASE_URL = f"http://{RASPI_HOSTNAME}:{PORT}"

# GET request: show all users
def get_users() -> list: # returns all users as list
    response = requests.get(BASE_URL+"/api/users")
    print( "Status Code  :", response.status_code)

    if response.ok: return response.json()
    else: return None

# GET request: show specific users, identified by id
def get_user( user_id: int ) -> dict: # returns a users
    response = requests.get(BASE_URL+f"/api/users/{user_id}")
    print( "Status Code  :", response.status_code)

    if response.ok: return response.json()
    else: return None

# POST request: create a new user
def create_user( user: dict ): # returns newly created user 
    response = requests.post( BASE_URL+"/api/users", json=user )
    print( "Status Code  :", response.status_code)

    if response.ok: return response.json()
    else: return None

# PUT request: update a user
def update_user( user_id: int, user: dict ): # returns newly created user
    response = requests.put( BASE_URL+f"/api/users/{user_id}", json=user)
    print( "Status Code  :", response.status_code)

    if response.ok: return response.json()
    else: return None

# DELETE request: delete user, identified by id
def delete_user(user_id):
    response = requests.delete( BASE_URL+f"/api/users/{user_id}" )
    print( "Status Code  :", response.status_code)

    if response.ok: return response.json()
    else: return None

if __name__ == "__main__":

    # get all users
    print("All users:\n",  get_users() )

    # get user with id 1
    print("User with id 1:\n", get_user(1) )

    # create user "DaisY" (deliberate typo!)
    new_user = {"name": "DaisY"}
    user =  create_user(new_user)
    print("User created:\n", user)

    # update user "DaisY" to "Daisy
    id = user["id"]
    user = {"name": "Daisy"}
    print("User updated:\n", update_user(id, user) )

    # get all users
    print("All users:\n", get_users() )

    # delete user by id
    id = 1
    print( f"Deleted user with id {id}:\n", delete_user(id) )

    # get all users
    print("All users:\n",  get_users() )

    # Testing ERRORs

    # get user with id 1, which was previously deleted
    assert get_user(id) == None, "Getting a non-existing user should return 'None'." 

    # delete user with id 1, which was already deleted
    assert delete_user(id) == None, "Getting a non-existing user should return 'None'."
from flask import Flask, jsonify, request

app = Flask(__name__)

# GET: hello world; DELETE: bye bye
@app.route("/api/hello", methods=["GET", "DELETE"])
def get_users():
    print( "Method: ", request.method ) # returns GET or DELETE
    if request.method == "GET": return jsonify( {"message":"Hello World!"} )
    else: return jsonify( {"message":"Bye, bye!"} )

if __name__ == "__main__":
    print( "Starting REST server" )
    app.run(host="0.0.0.0", debug=True) # run on all IP addresses


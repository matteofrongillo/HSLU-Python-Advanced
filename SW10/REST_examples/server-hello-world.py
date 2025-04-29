from flask import Flask, jsonify, request

app = Flask(__name__)

# GET: hello-world
@app.route('/api/hello', methods=['GET', 'DELETE'])
def get_users():
    print( "Method: ", request.method ) # returns GET or DELETE
    if request.method == 'GET': return jsonify( "Hello World!" )
    else: return jsonify( "Bye bye!" )

if __name__ == '__main__':
    print( "Starting REST server" )
    app.run(debug=True)
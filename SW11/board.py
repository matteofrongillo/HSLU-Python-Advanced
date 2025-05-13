from flask import Flask, request, jsonify
from flasgger import Swagger

if __name__ == "__main__":
    app = Flask(__name__)
    swagger = Swagger(app)

@app.route("/api/board", methods=["GET"])
def get_board():
    """
    Get the current state of the game board. (More API-documentation goes here!)
    ---
    tags:
    - Board API
    """
    board = [
    ["O", "O", "X"],
    ["-", "X", "O"],
    ["X", "O", "X"]]
    return jsonify( {"board": board} ), 200 # returns board as dict, code: 200 Ok
app.run(host="0.0.0.0", debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

transactions = []

@app.route("/transactions", methods=["POST"])
def add_transaction():
    data = request.get_json()
    user_id = int(data.get("user_id"))
    id = int(data.get("id"))
    amount = int(data.get("amount"))
    
    if not user_id or not id or not amount:
        return jsonify({"message": "Missing required fields"}), 400
    
    new_transaction = {"user_id": user_id, "id": id, "amount": amount}
    transactions.append(new_transaction)
    return jsonify({"message": "Transaction added", "transaction": new_transaction}), 201

@app.route("/api/users", methods=["GET"])
def get_transactions():
    return jsonify({"transactions": transactions})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

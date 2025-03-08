from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
data_store = {
    "items": []
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Python Backend API!"})

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json.get('item')
    if not item:
        return jsonify({"error": "Item is required"}), 400
    data_store["items"].append(item)
    return jsonify({"message": "Item added successfully", "item": item}), 201

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(data_store["items"]):
        removed_item = data_store["items"].pop(item_id)
        return jsonify({"message": "Item deleted successfully", "item": removed_item}), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
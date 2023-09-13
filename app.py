from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load the JSON data
with open('company.json', 'r') as f:
    data = json.load(f)

@app.route('/')
def homepage():
    return "This is the API homepage"

# Create a new company
@app.route('/create', methods=['POST'])
def create_company():
    new_company = request.json
    data.append(new_company)
    with open('comapny.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify({"message": "Company created successfully"}), 201

# Read all records
@app.route('/read', methods=['GET'])
def read_records():
    return jsonify(data)

# Read a specific record by ID
@app.route('/read/<int:record_id>', methods=['GET'])
def view_company(record_id):
    company = next((item for item in data if item["id"] == record_id), None)
    if company is not None:
        return jsonify(company)
    return jsonify({"message": "company not found"}), 404

# Update a company by ID
@app.route('/update/<int:record_id>', methods=['PUT'])
def update_company(record_id):
    updated_company = request.json
    for i, record in enumerate(data):
        if record["id"] == record_id:
            data[i] = updated_company
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
            return jsonify({"message": "Company updated successfully"})
    return jsonify({"message": "Conlmpany not found"}), 404

# Delete a company by ID
@app.route('/delete/<int:record_id>', methods=['DELETE'])
def delete_company(record_id):
    for i, record in enumerate(data):
        if record["id"] == record_id:
            del data[i]
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
            return jsonify({"message": "Company deleted successfully"})
    return jsonify({"message": "Company not found"}), 404

if __name__ == '__main__':
    app.run(port =5000, debug=True)

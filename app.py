from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'  # SQLite database
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/api', methods=['GET'])
def read_all_records():
    persons = Person.query.all()  # Retrieve all records from the Person table
    person_list = []

    for person in persons:
        person_data = {
            "id": person.id,
            "name": person.name,
            "age": person.age
        }
        person_list.append(person_data)
    return jsonify(person_list)

@app.route('/api/create', methods=['POST'])
def create_person():
    data = request.get_json()
    new_person = Person(name=data['name'], age=data['age'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"message": "Person created successfully"}), 201

@app.route('/api/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_person(user_id):
    person = Person.query.get_or_404(user_id)

    if request.method == 'GET':
        return jsonify({"name": person.name, "age": person.age})

    if request.method == 'PUT':
        data = request.get_json()
        person.name = data['name']
        person.age = data['age']
        db.session.commit()
        return jsonify({"message": "Person updated successfully"})

    if request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        return jsonify({"message": "Person deleted successfully"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)


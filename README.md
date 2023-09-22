# CRUD API for Managing Persons

This Markdown file provides detailed explanations for the functions in a Python script that implements a CRUD (Create, Read, Update, Delete) API for managing "person" resources using Flask and SQLAlchemy.

## Overview

The script defines a simple Flask application that allows you to perform CRUD operations on persons. It uses SQLite as the database system for data storage.

## Code Explanations

### Setting Up the Flask App and Database

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'  # SQLite database
db = SQLAlchemy(app)
```
We import Flask and SQLAlchemy to set up the Flask application and database.
We create a Flask app instance and configure it to use SQLite as the database with the URL 'sqlite:///persons.db'.
We initialize the SQLAlchemy extension with the Flask app to enable interaction with the database.

### Defining the Person Model
```python
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
```
We define a Person class that inherits from db.Model, which is a SQLAlchemy base class for creating database models.
The Person class represents the structure of a person, with attributes like id, name, and age. The id field serves as the primary key.

### Read all records in the database

```python
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
```
This route allows the reading of all the records in the database

### Creating a New Person (CREATE)

```python
@app.route('/api/create', methods=['POST'])
def create_person():
    data = request.get_json()
    new_person = Person(name=data['name'], age=data['age'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"message": "Person created successfully"}), 201
```
This route allows the creation of a new person.
It listens for HTTP POST requests at the endpoint /api.
It retrieves JSON data from the request using request.get_json().
It creates a new Person instance using the JSON data.
It adds the new person to the database session and commits the transaction.
It returns a JSON response with a success message and a status code 201 (Created).

### Reading Person Details (READ)

```python
@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get_or_404(user_id)
    return jsonify({"name": person.name, "age": person.age})
```
This route allows the retrieval of details for a specific person.
It listens for HTTP GET requests at the endpoint /api/<int:user_id>, where user_id is the unique identifier of the person.
It uses SQLAlchemy's query.get_or_404() method to retrieve the person by their ID from the database.
It returns a JSON response with the person's name and age.

### Updating Person Details (UPDATE)

```python
@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    person = Person.query.get_or_404(user_id)
    data = request.get_json()
    person.name = data['name']
    person.age = data['age']
    db.session.commit()
    return jsonify({"message": "Person updated successfully"})

```
This route allows the update of details for a specific person.
It listens for HTTP PUT requests at the endpoint /api/<int:user_id>, where user_id is the unique identifier of the person.
It retrieves the person by their ID from the database.
It updates the person's name and age using data from the JSON request.
It commits the changes to the database and returns a JSON response with a success message.

### Deleting a Person (DELETE)

```python
@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get_or_404(user_id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({"message": "Person deleted successfully"})
```
This route allows the deletion of a specific person.
It listens for HTTP DELETE requests at the endpoint /api/<int:user_id>, where user_id is the unique identifier of the person.
It gets the person by their ID from the database.
It deletes the person from the database session.
It commits the transaction and returns a JSON response with a success message.

### How to run this flask application

```python
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
NOTE: The api has been deployed on ngrok, the tunnel expires after between 1-2 hours. 




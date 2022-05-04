import os
import flask_mongoengine
import pymongo
from bson import ObjectId
from bson.json_util import dumps, loads
from flask import Flask, Response, request, render_template
from datetime import datetime
import json

app = Flask(__name__)

MONGODB_URI = 'mongodb://localhost:27017'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']


@app.route('/api/v1.0/students', methods=['GET'])
def students():
    students = db.students.find()
    return Response(dumps(students), mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    student = db.students.find({'_id': ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')


@app.route('/students/add')
def add_student():
    return render_template('add.html')


@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        "name": name,
        "country": country,
        "city": city,
        "birthyear": birthyear,
        "skills": skills,
        "bio": bio,
        "created_at": created_at

    }
    db.students.insert_one(student)
    return


@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    query = {"_id": ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    return


@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    db.students.delete_one({"_id":ObjectId(id)})
    return


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

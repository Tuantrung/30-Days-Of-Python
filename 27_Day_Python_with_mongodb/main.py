# let's import the flask
import pymongo
from flask import Flask, render_template
import os # importing operating system module
MONGODB_URI = "mongodb://localhost:27017"
client = pymongo.MongoClient(MONGODB_URI)

db = client['thirty_days_of_python']
db.students.drop()

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
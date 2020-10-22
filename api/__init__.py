import os

from ariadne import QueryType
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

query = QueryType()


@app.route('/')
def hello():
    return 'Hello!'


if __name__ == '__main__':
    app.run(debug=True)

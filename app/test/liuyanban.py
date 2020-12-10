import os
import string
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, flash
import sqlite3 as sql
import random

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    content = db.Column(db.String(64))

    def __init__(self, username, content):
        self.username = username
        self.content = content

    def __repr__(self):
        return '<Message %r>' % self.content


@app.route('/')
def home():
    return render_template("message.html")


@app.route('/message')
def message():
    return render_template("message.html")


@app.route('/submit_message', methods=['GET', 'POST'])
def submit_message():
    if request.method == 'POST':
        data = request.data.decode()
        d = eval(data)
        username = ''.join(random.sample(string.ascii_letters + string.digits, 7))
        content = d['content']
        newmessage = Message(username, content)
        db.session.add(newmessage)
        db.session.commit()
        return render_template('message.html')
    else:
        return render_template('message.html')


@app.route('/read_message')
def readmessage():
    con = sql.connect("data.sqlite")
    con.row_factory = sql.Row
    cur = con.cursor()
    cursor = cur.execute("select username, content from message")
    res = ''
    for row in cursor:
        res = res + ' ' + str(row[0]) + ' ' + str(row[1])
    return res


db.create_all()

if __name__ == '__main__':
    db.create_all()
    app.run()


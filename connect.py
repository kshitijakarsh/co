from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:kshitij29@127.0.0.1/sih'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class drone_side_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Decimal(10,8), nullable=False)
    latitude = db.Column(db.Decimal(11,8), nullable=False)
    what3words = db.Column(db.VARCHAR(255), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
    
class website_data_entry_side_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Decimal(10,8), nullable=False)
    latitude = db.Column(db.Decimal(11,8), nullable=False)
    what3words = db.Column(db.VARCHAR(255), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/auth_construction')
def authorized_construction():
    data1 = drone_side_table.query.all()
    data2 = website_data_entry_side_table.all()
    return render_template('show_users.html', data1=data1, data2=data2)


if __name__ == '__main__':
    app.run(debug=True)

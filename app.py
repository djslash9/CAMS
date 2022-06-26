from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    location = db.Column(db.String(100))
    type = db.Column(db.String(100))
    cluster = db.Column(db.String(100))
    se = db.Column(db.String(100))
    status = db.Column(db.String(100))
    
    def __init__(self, name, email, phone, location, type, cluster, se, status):
    
        self.name = name
        self.email = email
        self.phone = phone
        self.location = location
        self.type = type
        self.cluster = cluster
        self.se = se
        self.status = status

#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template('index.html', employees = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        location = request.form['location']
        type = request.form['type']
        cluster = request.form['cluster']
        se = request.form['se']
        status = request.form['status'] 

        my_data = Data(name, email, phone, location, type, cluster, se, status)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))
    
@app.route('/update', methods = ['POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        my_data.location = request.form['location']
        my_data.type = request.form['type']
        my_data.cluster = request.form['cluster']
        my_data.se = request.form['se']
        my_data.status = request.form['status']         
        
        db.session.commit()
        flash("Employee updated successfully")
        
        return redirect(url_for('Index'))
    
@app.route('/delete/<id>', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    
    db.session.delete(my_data)
    db.session.commit()

    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))
if __name__ == "__main__":
    app.run(debug=True)
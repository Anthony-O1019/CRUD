from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")
            
@app.route('/create_user', methods=["POST"])
def create_user():
    if not User.validate_user(request.form):
        redirect('/')
        
    if not User.validate_user(request.form):
        return redirect('/')

    User.save(request.form)
    print(request.form)
    return redirect('/process')

@app.route('/process')
def user():
    users = User.get_all() 
    print(users) 
    return render_template('read(all).html',users = User.get_all()) 

from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models import ninja

@app.route('/dojo')
def task1():
    alldojos = Dojo.get_all()
    return render_template("dojo.html", all_dojos = alldojos)

@app.route('/createdojo', methods=['POST'])
def task4():
    data = {
        "name": request.form["name"]
    }

    Dojo.save_dojo(data)

    return redirect('/dojo')

@app.route('/showdojo/<int:dojo_id>')
def task3(dojo_id):
    data = {
        'id': dojo_id
    }
    
    alldojo = Dojo.get_one(data)
    print(alldojo.name)
    return render_template('showdojo.html', alldojo = alldojo, dojos = Dojo.get_dojo_with_ninjas(data))


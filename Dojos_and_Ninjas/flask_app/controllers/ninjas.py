from crypt import methods
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models import ninja


@app.route('/ninjas')
def create_ninja():

    return render_template('newninja.html', dojos = Dojo.get_all())

@app.route('/addninja', methods=["POST"])
def task2():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }

    ninja.Ninja.save(data)

    return redirect('/dojo')

@app.route('/deleteninja/<int:ninja_id>')
def task5(ninja_id):
    data = {
        'id': ninja_id
    }
    

    ninja.Ninja.delete_ninja(data)

    print(data)
    return redirect('/dojo')

@app.route('/editninja')
def task6():
    data = {
        'first_name': ninja.Ninja.self.first_name
    }
    ninja.Ninja.get_all(data)
    print(ninja.Ninja.first_name)
    return render_template('edit.html')
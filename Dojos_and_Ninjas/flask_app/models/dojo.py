from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_one(cls,data):
        query= "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return cls(result[0])

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        dojo  = cls( results[0])
        for row_from_data in results:
            ninja_data = {
            "id": row_from_data["ninjas.id"],
            "first_name": row_from_data["first_name"],
            "last_name": row_from_data["last_name"],
            "age": row_from_data["age"],
            "created_at": row_from_data["ninjas.created_at"],
            "updated_at": row_from_data["ninjas.updated_at"]
        }
        new_ninja = Ninja(ninja_data)
        dojo.ninjas.append( new_ninja )
        return dojo

    @classmethod
    def delete_dojo():
        query = "DELETE FROM dojos WHERE id = %(id)s"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        return result
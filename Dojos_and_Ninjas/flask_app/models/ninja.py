from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        ninjas = []

        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data):
        # try inputting the query into workbench to make sure that the query is correct.
        # Getting error "Something went wrong (1364, "Field 'dojo_id' doesn't have a default value")"
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(),NOW());"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def delete_ninja(cls,data):

        query = "DELETE FROM ninjas WHERE id = %(id)s"

        result =  connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        return result
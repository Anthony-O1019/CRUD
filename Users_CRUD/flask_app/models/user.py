from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(user)
        return users
            
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users_schema').query_db( query, data )

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['fname']) < 3:
            flash("Name does not have enough characters!")
            is_valid = False
        if len(user['lname']) < 3:
            flash("Name does not have enought characters!")
            is_valid = False
        
        return is_valid
    @staticmethod
    def validate_user(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email Address')
            is_valid = False
        return is_valid

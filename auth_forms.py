from flask import request, flash
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, ValidationError
from sql_queries.user_queries import GET_USER_BY_USERNAME, GET_USER_BY_EMAIL
from database_info import create_connection

# USER CLASS
class User(UserMixin):
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        
    def get_id(self):
        return str(self.id)
    
# REGISTER FORM
class register_form(FlaskForm): 
    # WTFORMS - FIELDS 
    username = StringField(
        validators=[
            InputRequired(),
        ]
    )
    password = PasswordField(validators=[InputRequired(), Length(8,72)])
    email = StringField(validators=[InputRequired(), Email()])
    
    # EMAIL VALIDATION
    def validate_email(self,email):
        # DB CONNECTION
        conn = create_connection()
        
        email = request.form['email']
        # CREATE CURSOR
        cur = conn.cursor()
        # SELECT ALL FROM USERS - EMAIL
        cur.execute(GET_USER_BY_EMAIL, (email, ))
        user = cur.fetchone()
        # CLOSE THE CURSOR AND CONNECTION
        cur.close()
        conn.close()
        if user:
            flash("Email already taken!", "error")
        
    # USERNAME VALIDATION
    def validate_username(self,username):
        # DB CONNECTION
        conn = create_connection()
        
        username = request.form['username']
        # CREATE CURSOR
        cur = conn.cursor()
        cur.execute(GET_USER_BY_USERNAME, (username, ))
        # FETCH ONE
        user = cur.fetchone()
        # CLOSE THE CURSOR AND CONNECTION
        cur.close()
        conn.close()
        if user:
            raise ValidationError("Username is already taken")
        
# LOGIN FORM
class login_form(FlaskForm):
    # WTFORMS - FIELDS
    username = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired(), Length(8,72)])
    
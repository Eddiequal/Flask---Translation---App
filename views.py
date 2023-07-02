from flask import Blueprint, render_template
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from wtforms import validators
from flask_login import current_user, login_user, login_required, logout_user
from auth_forms import register_form, login_form
from auth_forms import User
from deep_translator import GoogleTranslator
from database_info import create_connection
from sql_queries.user_queries import INSERT_USER_INFO, GET_USER_BY_USERNAME
from sql_queries.word_queries import GET_WORDS_BY_USER_ID, INSERT_WORD_INFO, UPDATE_WORD_INFO, DELETE_WORDS_BY_USER_ID

views = Blueprint('view', __name__)

# INDEX ROUTE
@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# REGISTER ROUTE 
@views.route('/register', methods=['GET', 'POST'])
def register(): 
    # REGISTER FORM 
    form = register_form(request.form)
    # FORM VALIDATION
    if form.validate():
        try:
            # DB CONNECTION
            conn = create_connection()
    
            cur = conn.cursor()
            # REQUEST FORM
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            # INSERT INTO USERS
            cur.execute(INSERT_USER_INFO, (username, password, email))
            #COMMIT CHANGES
            conn.commit()
            # CLOSE THE CURSOR AND CONNECTION
            cur.close()
            conn.close()
            # FLASH MESSAGE
            flash("Account Succesfully created", "success")
            return redirect(url_for('login'))
        except Exception as e:
            flash(str(e), "danger")
    return render_template('register.html', form=form)
    
# LOGIN ROUTE
@views.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Dictionary'))
    # LOGIN FORM
    form = login_form(request.form)
    # FORM VALIDATION
    if form.validate():
        # DB CONNECTION
        conn = create_connection()
        
        cur = conn.cursor()
        # REQUEST FORM
        username = request.form['username']
        
        session['username'] = request.form['username']
        # SELECT ALL FROM USERS - USERNAME
        cur.execute(GET_USER_BY_USERNAME, (username,))
        #FETCH ONE
        user = cur.fetchone()
        # CLOSE THE CURSOR AND CONNECTION
        cur.close()
        conn.close()
        
        if user is not None:
            user = User(user[0], user[1], user[2], user[3])
            login_user(user)
            return redirect(url_for('view.dictionary'))
        
        flash("Invalid username or password", "error")
        
    return render_template('login.html', form=form)

@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('view.index'))

# DICTIONARY ROUTE
@views.route('/Dictionary', methods = ['GET', 'POST'])
@login_required
def dictionary():
    # DB CONNECTION
    conn = create_connection()
    
    cur = conn.cursor()
     
    if 'username' in session:
        # SELECT ALL FROM THE TABLE
        user_id = current_user.id
        
        cur.execute(GET_WORDS_BY_USER_ID, (user_id,))
        
        conn.commit()
        # FETCH ALL
        data = cur.fetchall()
        session['username'] = data
        # CLOSE THE CURSOR AND CONNECTION
        cur.close()
        conn.close()

        return render_template('dictionary.html', data = session['username'])
    else:
        return redirect(url_for('view.login', first_lang='default'))
    
# DICTIONARY CREATE ROUTE
@views.route('/create', methods = ['POST'])
def create():
    # DB CONNECTION
    conn = create_connection()
    # CREATE CURSOR
    cur = conn.cursor()
    #REQUEST FORM 
    Definition = request.form['Definition']
    Meaning = request.form['Meaning']
    user_id = current_user.id
    
    first_lang = request.form['first_lang']
    second_lang = request.form['second_lang']
    # GOOGLE TRANSLATOR
    res = GoogleTranslator(source=f'{first_lang}', target=f'{second_lang}').translate(f"{Definition}")
    Meaning = res

    # INSERT THE DATA INTO THE WORDS TABLE
    cur.execute(INSERT_WORD_INFO,(Definition, Meaning, user_id,))
    
    # COMMIT CHANGES
    conn.commit()
    # CLOSE THE CURSOR AND CONNECTION
    cur.close()
    conn.close()
    return redirect(url_for('view.dictionary', first_lang=first_lang))

# DICTIONARY UPDATE ROUTE
@views.route('/update', methods = ['POST'])
def update():
    # DB CONNECTION
    conn = create_connection()
    # CREATE CURSOR
    cur = conn.cursor()
    # REQUEST FORM
    Definition = request.form['Definition']
    Meaning = request.form['Meaning']
    id = request.form['id']
    
    # UPDATE WORDS SET - DEFINITON, MEANING, ID
    cur.execute(UPDATE_WORD_INFO, (Definition, Meaning, id))
    # COMMIT CHANGES
    conn.commit()    
    return redirect(url_for('view.dictionary'))

# DICTIONARY DELETE ROUTE
@views.route('/delete', methods = ['POST'])
def delete():
    # DB CONNECTION
    conn = create_connection()
    # CREATE CURSOR
    cur = conn.cursor()
    # REQUEST FORM
    id = request.form['id']
    # DELETE ALL FROM WORDS - ID
    cur.execute(DELETE_WORDS_BY_USER_ID, (id,))
    # COMMIT CHANGES
    conn.commit()
    # CLOSE THE CURSOR AND CONNECTION
    cur.close()
    conn.close()
    
    return redirect(url_for('view.dictionary'))
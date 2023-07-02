from sql_queries.user_queries import GET_USER_BY_ID
from config import app, login_manager
from database_info import create_connection
from auth_forms import User
from views import views


app.register_blueprint(views)
 
# USER LOADER
@login_manager.user_loader
def load_user(id):
    # DB CONNECTION
    conn = create_connection()
    
    cursor = conn.cursor()
    # SELECT ALL FROM USERS - id
    cursor.execute(GET_USER_BY_ID, (id,))
    # FETCH ONE
    user = cursor.fetchone()
    # CLOSE THE CURSOR AND CONNECTION
    cursor.close()
    conn.close()

    if user is not None:
        user = User(user[0], user[1], user[2], user[3])
        return user 
    
    return None 


# main driver function
if __name__ == '__main__':
    app.run(debug=True)
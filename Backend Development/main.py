from flask import Flask, render_template, request, redirect, url_for
from user_login import get_logged_in_user, register_user
from movies import movies_bp, get_movies  # Import the movies Blueprint and get_movies function
import mysql.connector

app = Flask(__name__, template_folder='C:\\Users\\reddy\\Movies Recommend Website Project\\templates\\Frontend Development', static_folder='C:\\Users\\reddy\\Movies Recommend Website Project\\templates\\static')

# Database connection
mydb = mysql.connector.connect(
        host="127.0.0.3",
        user="root",
        password="123456789",
        database="MovieDB"
)

# Register the movies Blueprint
app.register_blueprint(movies_bp, url_prefix='/movies')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mobile_number = request.form['mobile_number']
        if register_user(username, password, mobile_number):
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error='Username already exists')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if get_logged_in_user(username, password):
            return redirect(url_for('welcome', username=username))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

@app.route('/home')
def home():
    return render_template('home.html')

def get_movies(category, sort_by='release_date'):
    cursor = mydb.cursor()
    
    # Map sort_by values to corresponding SQL column names
    sort_columns = {
        'release_date': 'release_date',
        'ratings': 'ratings',
        'ott_platform': 'ott_platform'
    }
    
    if sort_by in sort_columns:
        sort_column = sort_columns[sort_by]
    else:
        sort_column = 'release_date'  # Default sorting
    
    query = f"""
        SELECT movie_name, cast, summary, release_date, ratings, ott_link, ott_platform 
        FROM {category.lower()}_movies 
        ORDER BY {sort_column} DESC
    """
    cursor.execute(query)
    movies = cursor.fetchall()
    return movies

@app.route('/catalog/<category>')
def catalog(category):
    sort_by = request.args.get('sort_by', 'release_date')
    movies = get_movies(category, sort_by)
    return render_template('catalog.html', category=category, movies=movies)

if __name__ == '__main__':
    app.run(debug=True)

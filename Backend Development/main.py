from flask import Flask, render_template, request, redirect, url_for
from user_login import get_logged_in_user, register_user
from admin_login import admin_login  # Import the admin_login function
from movies import movies_bp, get_movies  # Import the movies Blueprint and get_movies function
import mysql.connector

app = Flask(__name__, template_folder='C:\\Users\\reddy\\Movies Recommend Website Project\\templates\\Frontend Development', static_folder='C:\\Users\\reddy\\Movies Recommend Website Project\\templates\\static')

# Database connection
db_config = {
    'host': '127.0.0.3',
    'user': 'root',
    'password': '123456789',
    'database': 'MovieDB'
}
mydb = mysql.connector.connect(**db_config)

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
        if admin_login(username, password):
            return redirect(url_for('admin_dashboard'))
        elif get_logged_in_user(username, password):
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
        SELECT movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category
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

@app.route('/admin_dashboard')
def admin_dashboard():
    cursor = mydb.cursor()
    categories = ['Telugu', 'Hindi', 'English']
    movies_by_category = {category: get_movies(category) for category in categories}
    return render_template('admin_dashboard.html', movies_by_category=movies_by_category)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        category = request.form['category']
        movie_name = request.form['movie_name']
        cast = request.form['cast']
        summary = request.form['summary']
        release_date = request.form['release_date']
        ratings = request.form['ratings']
        ott_link = request.form['ott_link']
        ott_platform = request.form['ott_platform']
        cursor = mydb.cursor()
        query = f"""
            INSERT INTO {category.lower()}_movies 
            (movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category))
        mydb.commit()
        return redirect(url_for('admin_dashboard'))
    return render_template('add_movie.html')

@app.route('/edit_movie/<category>/<movie_name>', methods=['GET', 'POST'])
def edit_movie(category, movie_name):
    cursor = mydb.cursor()
    if request.method == 'POST':
        new_movie_name = request.form['movie_name']
        cast = request.form['cast']
        summary = request.form['summary']
        release_date = request.form['release_date']
        ratings = request.form['ratings']
        ott_link = request.form['ott_link']
        ott_platform = request.form['ott_platform']
        query = f"""
            UPDATE {category.lower()}_movies 
            SET movie_name=%s, cast=%s, summary=%s, release_date=%s, ratings=%s, ott_link=%s, ott_platform=%s 
            WHERE movie_name=%s
        """
        cursor.execute(query, (new_movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, movie_name))
        mydb.commit()
        return redirect(url_for('admin_dashboard'))
    query = f"SELECT * FROM {category.lower()}_movies WHERE movie_name=%s"
    cursor.execute(query, (movie_name,))
    movie = cursor.fetchone()
    return render_template('edit_movie.html', movie=movie)

@app.route('/delete_movie/<category>/<movie_name>')
def delete_movie(category, movie_name):
    cursor = mydb.cursor()
    query = f"DELETE FROM {category.lower()}_movies WHERE movie_name=%s"
    cursor.execute(query, (movie_name,))
    mydb.commit()
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)

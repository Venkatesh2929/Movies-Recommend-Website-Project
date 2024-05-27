import mysql.connector
from flask import render_template, Blueprint, redirect, url_for, request

movies_bp = Blueprint('movies', __name__)

# Connect to the database
mydb = mysql.connector.connect(
    host="127.0.0.3",
    user="root",
    password="123456789",
    database="MovieDB"
)

# Function to fetch movie data from the database based on category
def get_movies(category):
    cursor = mydb.cursor()
    query = "SELECT movie_name, cast, summary, release_date, ratings, ott_link, ott_platform FROM {} WHERE category = %s".format(category.lower() + "_movies")
    cursor.execute(query, (category,))
    movies = cursor.fetchall()
    return movies

@movies_bp.route('/')
def movies():
    return render_template('movies.html')

@movies_bp.route('/redirect_to_ott')
def redirect_to_ott():
    ott_platform = request.args.get('ott_platform')
    ott_link = request.args.get('ott_link')
    
    ott_homepages = {
        "PrimeVideos": "https://www.primevideo.com",
        "Zee5": "https://www.zee5.com",
        "Appletv+": "https://www.apple.com/apple-tv-plus",
        "Netflix": "https://www.netflix.com",
        "Hotstar": "https://www.hotstar.com",
        "JioCinemas": "https://www.jiocinema.com"
    }
    
    if ott_platform in ott_homepages:
        return redirect(ott_homepages[ott_platform])
    else:
        return redirect(ott_link)

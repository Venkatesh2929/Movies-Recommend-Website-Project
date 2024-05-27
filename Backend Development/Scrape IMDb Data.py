import requests
from bs4 import BeautifulSoup
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="127.0.0.3",
    user="root",
    password="123456789",
    database="MovieDB"
)

# Function to scrape movie data from IMDb and save to database
def scrape_and_save(url, category, table_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []

    if category == 'English':
        items = soup.select('.lister-item')
    elif category == 'Telugu':
        items = soup.select('.lister-list .titleColumn')
    elif category == 'Hindi':
        items = soup.select('.lister-list .lister-item')
    
    for item in items:
        if category == 'English':
            movie_name = item.h3.a.text.strip()
            cast = item.find('p', class_='').text.strip()
            summary = item.find_all('p', class_='text-muted')[1].text.strip()
            release_date = item.find('span', class_='lister-item-year').text.strip()
            ratings = item.find('div', class_='inline-block ratings-imdb-rating').strong.text.strip()
            ott_link = "https://www.imdb.com" + item.h3.a['href']
            ott_platform = 'IMDb'
        elif category == 'Telugu':
            movie_name = item.a.text.strip()
            cast = 'N/A'  # You might need another way to get this information
            summary = 'N/A'
            release_date = item.find('span', class_='secondaryInfo').text.strip()
            ratings = item.find_next('strong').text.strip()
            ott_link = "https://www.imdb.com" + item.a['href']
            ott_platform = 'IMDb'
        elif category == 'Hindi':
            movie_name = item.h3.a.text.strip()
            cast = item.find('p', class_='').text.strip()
            summary = item.find_all('p', class_='text-muted')[1].text.strip()
            release_date = item.find('span', class_='lister-item-year').text.strip()
            ratings = item.find('div', class_='inline-block ratings-imdb-rating').strong.text.strip()
            ott_link = "https://www.imdb.com" + item.h3.a['href']
            ott_platform = 'IMDb'
        
        movies.append((movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category))

    # Insert data into the database
    cursor = mydb.cursor()
    insert_query = f"""
    INSERT INTO {table_name} (movie_name, cast, summary, release_date, ratings, ott_link, ott_platform, category)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(insert_query, movies)
    mydb.commit()
    cursor.close()

# Scrape and save English movies
scrape_and_save('https://m.imdb.com/chart/top-english-movies/', 'English', 'english_movies')

# Scrape and save Telugu movies
scrape_and_save('https://www.imdb.com/india/top-rated-telugu-movies/', 'Telugu', 'telugu_movies')

# Scrape and save Hindi movies
scrape_and_save('https://www.imdb.com/search/title/?title_type=feature&countries=IN&languages=hi', 'Hindi', 'hindi_movies')

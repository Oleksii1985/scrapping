import requests
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h2")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

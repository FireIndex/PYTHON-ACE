# Plote IMDb Top Movies Ratings Over Years.py

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Function to scrape movie data from IMDb
def scrape_imdb_top_movies():
    url = "https://www.imdb.com/chart/top"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    movies = []
    for movie_row in soup.find_all("li", class_="ipc-metadata-list-summary-item"):
        try:
            title = movie_row.find("h3", class_="ipc-title__text").text
            rating = float(movie_row.find("span", class_="ipc-rating-star").text)
            year = int(movie_row.find("span", class_="cli-title-metadata-item").text.strip("()"))
            movies.append({"title": title, "rating": rating, "year": year})
        except:
            continue
    
    # store_movie_data_csv(movies)
    
    return movies

def store_movie_data_csv(movies):
    with open("imdb_top_movies.csv", "w", encoding="utf-8") as f:
        f.write("Title\tRating\tYear\n")
        for movie in movies:
            f.write(f"{movie['title']}\t{movie['rating']}\t{movie['year']}\n")


# Function to analyze and visualize movie data
def analyze_and_visualize_movies(movies):
    ratings = [movie["rating"] for movie in movies]
    years = [movie["year"] for movie in movies]

    average_rating = sum(ratings) / len(ratings)
    highest_rated = max(movies, key=lambda x: x["rating"])
    num_movies_per_year = {year: years.count(year) for year in set(years)}

    print(f"Average Rating: {average_rating:.2f}")
    print(f"Highest Rated Movie: {highest_rated['title']} ({highest_rated['rating']})")
    
    plt.figure(figsize=(10, 6))
    plt.scatter(years, ratings, alpha=0.5)
    plt.title("IMDb Top Movies Ratings Over Years")
    plt.xlabel("Year")
    plt.ylabel("Rating")
    plt.show()

def main():
    print("Scraping IMDb Top Movies...")
    movies = scrape_imdb_top_movies()
    print("Data Scraped for", len(movies), "movies.")
    print("Analyzing and Visualizing Movie Data...")
    analyze_and_visualize_movies(movies)

if __name__ == "__main__":
    main()

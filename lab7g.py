# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 11/13/2026
# Purpose: Create data frame from CSV file.
# Usage: ./lab7g.py

import pandas as pd
import matplotlib.pyplot as plt

# TO DO 1: create a new data frame from the link of csv file provided in readme.md file.
movies = pd.read_csv("./imdb_top_250.csv")
# TO DO 2: Perform the operations provided in readme.md file on this data frame.
# Print summary of the data contained in data frame
print("Summary of the data:")
print(movies.describe)
# Print first 10 and last 10 rows of this data frame
print("\nFirst 10 Movies:")
print(movies.head(10))

print("\nLast 10 Movies:")
print(movies.tail(10))
# Using operation on data frame print the year of earliest and latest movie
print("\nEarliest movie year:", movies["Year"].min())
print("Latest movie year:", movies["Year"].max())
# Print unique values in the "Genre" column
print("\nUnique Genres:")
print(movies["Genre"].unique())
# Count how many movies are not made in the USA
list_not_usa_movies = movies[movies["Origin"] != "USA"]
print("Movies not made in USA:", len(list_not_usa_movies))
# Find top 10 highest-rated movies
top_movies = movies.sort_values(by="IMDB rating", ascending=False)
print(top_movies.head(10))
# Find out what the best decade of movies is. Also display using a scatter plot
# Follow:
# Step 1. First define a python function that gets the decade from the year
def get_decade(year):
    return (year // 10) * 10
# Step 2. Add a decade column to the dataframe
movies["Decade"] = movies["Year"].apply(get_decade)
# Step 3. Group by decade to get the mean rating for each decade
decade_ratings = movies.groupby("Decade")["IMDB rating"].mean()

print("Average rating by decade:")
print(decade_ratings)

print("Best decade:", decade_ratings.idxmax())
# Step 4. Create a scatter plot using MATPLOT
plt.scatter(decade_ratings.index.to_numpy(), decade_ratings.to_numpy())
plt.title("Average IMDB Rating by Decade")
plt.xlabel("Decade")
plt.ylabel("Average Rating")
plt.show()
# TO DO 3: Run the script.

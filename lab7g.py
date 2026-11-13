# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 11/13/2026
# Purpose: Create data frame from CSV file.
# Usage: ./lab7g.py

import pandas as pd
import matplotlib.pyplot as plt

# TO DO 1: create a new data frame from the link of csv file provided in readme.md file.
url = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"
df = pd.read_csv(url, index_col=0)
# TO DO 2: Perform the operations provided in readme.md file on this data frame.
# Print summary of the data contained in data frame
print("Summary of the data:")
print(df.describe(include="all"))
# Print first 10 and last 10 rows of this data frame
print("\nFirst 10 Movies:")
print(df.head(10))

print("\nLast 10 Movies:")
print(df.tail(10))
# Using operation on data frame print the year of earliest and latest movie
print("\nEarliest movie year:", df["Year"].min())
print("Latest movie year:", df["Year"].max())
# Print unique values in the "Genre" column
print("\nUnique Genres:")
print(df["Genre"].unique())
# Count how many movies are not made in the USA
non_usa_movies = df[
    ~df["Origin"].str.contains(r"\bUSA\b", na=False)
]
print("\nNumber of movies not made in USA:")
print(len(non_usa_movies))
# Find top 10 highest-rated movies
top_10 = df.sort_values(
    by="IMDB rating",
    ascending=False
).head(10)

print("\nTop 10 highest-rated movies:")
print(top_10[["Title", "Year", "IMDB rating"]])
# Find out what the best decade of movies is. Also display using a scatter plot
# Follow:
# Step 1. First define a python function that gets the decade from the year
def get_decade(year):
    return (year // 10) * 10
# Step 2. Add a decade column to the dataframe
df["Decade"] = df["Year"].apply(get_decade)
# Step 3. Group by decade to get the mean rating for each decade
decade_ratings = df.groupby("Decade")["IMDB rating"].mean()

best_decade = decade_ratings.idmax()
best_rating = decade_ratings.max()
print("\nBest Decade:", int(best_decade), "s")
# Step 4. Create a scatter plot using MATPLOT
plt.scatter(decade_ratings.index, decade_ratings.values)
plt.title("Average IMDb Movie Rating by Decade")
plt.xlabel("Decade")
plt.ylabel("Average IMDb Rating")

plt.xticks(decade_ratings.index, rotation=45)
plt.grid(True)

plt.show()
# TO DO 3: Run the script.

#teacher

movies=pd.read_csv("./imdb_top_250.csv")
print(movies.head(10))
print(movies.tail(10))
print(movies.columns)
print("Earliest movie:", movies['Year'].min())
print(movies['Genre'].unique())
list_not_usa_movies=movies[movies["Origin"]!="USA"]
print(len(list_not_usa_movies))
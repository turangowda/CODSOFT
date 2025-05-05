# Sample movie dataset with genres
movies = {
     "KGF2": ["Action"],
    "Salaar": ["Action"],
    "LEO": ["Action"],
    "SITA RAMAM": ["Romance", "Drama"],
    "HI NANNA": ["Romance", "Drama"],
    "ENTHIRAN": ["Sci-fi", "Action"],
    "KALKI": ["Sci-fi", "Action","Mythological"],
    "24":["sci-fi","Action"],
    "KANTARA":["Action","Adventure","Drama"],
    "Kanchana":["Horror","Thriller"],
    "Tumbad":["Horror","Fantasy","Thriller"],
    "Akhanda":["Mythological"],
    "Hanuman":["Mythological","Adventure","Fantasy"],
}

# Function to get movie recommendations based on a preferred genre
def recommend_movies(favorite_movie):
    if favorite_movie not in movies:
        print("Sorry, movie not found in our database.")
        return []

    favorite_genres = movies[favorite_movie]
    recommendations = []

    for movie, genres in movies.items():
        if movie != favorite_movie and any(genre in favorite_genres for genre in genres):
            recommendations.append(movie)

    return recommendations

# Example usage
user_movie = input("Enter a movie you like: ")
recommendations = recommend_movies(user_movie)

if recommendations:
    print("You might also like:", ", ".join(recommendations))
else:
    print("No recommendations found.")

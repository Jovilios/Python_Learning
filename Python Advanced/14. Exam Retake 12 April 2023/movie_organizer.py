def movie_organizer(*args):
    movies = {}

    for movie, gener in args:
        if gener not in movies:
            movies[gener] = []
        movies[gener].append(movie)

    sorted_movies_by_genres = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))

    output = ""

    for genre, film_name in sorted_movies_by_genres:
        movies_in_genre = sorted(film_name)
        output += f"{genre} - {len(movies_in_genre)}\n"
        for movie in sorted(movies_in_genre):
            output += f"* {movie}\n"

    return output.strip()






print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

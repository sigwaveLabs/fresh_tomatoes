import webbrowser


class Movie():

    def __init__(self, movie_title,
                 movie_year, movie_rating,
                 movie_genre, movie_storyline,
                 poster_image, trailer_youtube):
        """Creates an instance of the movie class.
        Args:
            movie_title: The title of the movie.
            movie_year: The year the movie was released.
            movie_rating: The rating of the movie.
            movie_genre: The genre of the movie.
            movie_storyline: The plot or storyline of the movie.
            poster_image: A link to the movie poster image.
            trailer_youtube: A link to the youtube movie trailer.
        Returns:
            A movie object instance.
        """
        self.title = movie_title
        self.year = movie_year
        self.rating = movie_rating
        self.genre = movie_genre
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens youtube trailer for movie"""

        webbrowser.open(self.trailer_youtube_url)

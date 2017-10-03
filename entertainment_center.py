import media
import fresh_tomatoes


the_castle = media.Movie("The Castle",
                         "1997",
                         "R",
                         "Comedy",
                         "A working-class family from Melbourne, Australia fights city hall after being told they must vacate their beloved family home to allow for infrastructural expansion.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY1MTk5Mzk0M15BMl5BanBnXkFtZTYwMzgxNjQ5._V1_SX300.jpg",
                         "https://www.youtube.com/watch?v=rpqT_l7QcBM")

cujo = media.Movie("Cujo",
                         "1983",
                         "R",
                         "Horror",
                         "Cujo, a friendly St. Bernard, contracts rabies and conducts a reign of terror on a small American town.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BY2ZlMWNiODYtYjMwOS00OWQ0LWFiZDEtNmFlYTUzMjA2MzNmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg",
                         "https://www.youtube.com/watch?v=v0k21yeVMbM")

the_jerk = media.Movie("The Jerk",
                         "1979",
                         "R",
                         "Comedy",
                         "An idiotic man struggles to make it through life on his own in St. Louis.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BZDNmNThjMTMtNzVlZC00MzgyLWE3M2UtNGQ3ZTZmNjM3YWI2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg",
                         "https://www.youtube.com/watch?v=lduFFNqBFPs")
the_blues_brothers = media.Movie("The Blues Brothers",
                         "1980",
                         "R",
                         "Comedy",
                         "Jake Blues, just out from prison, puts together his old band to save the Catholic home where he and brother Elwood were raised.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMzdhOTJmYmQtMmE0OS00ZDMyLWFkZDItZmZmMGJlNGUyNjNhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SX300.jpg",
                         "https://www.youtube.com/watch?v=2HCR4c1zPyk")

the_burbs = media.Movie("The 'Burbs",
                         "1989",
                         "PG",
                         "Comedy",
                         "An overstressed suburbanite and his fellow neighbors are convinced that the new family on the block are part of a murderous Satanic cult.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNWE1OGExYzQtYzRjOS00MmJhLWE3OTYtZjkzOTNlMjJlZTQ4L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyODY0NzcxNw@@._V1_SX300.jpg",
                         "https://www.youtube.com/watch?v=Z3lfkZTwN00")

the_goonies = media.Movie("The Goonies",
                         "1985",
                         "PG",
                         "Adventure",
                         "In order to save their home from foreclosure, a group of misfits set out to find a pirate's ancient valuable treasure.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BOTlmMWU5YTQtOWMxMi00OWE0LTg2MDItMjEyZDBjNWY0NDdhL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg",
                         "https://www.youtube.com/watch?v=hJ2j4oWdQtU")

movies = [the_blues_brothers, the_burbs, the_castle, cujo, the_goonies, the_jerk, ]

fresh_tomatoes.open_movies_page(movies)

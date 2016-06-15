# This allows us to import the file that makes the different movies display as a webpage.
import fresh_tomatoes
# This allows us to import the class defined in media and make use of it
import media

# The followings are instances use to showcase the class 'Movie'. All the movies listed have the required variables as sepcified when
# building the class Movie (self,movie_title,movie_storyline,poster_image,trailer_youtube)
# self in this case is the movie and does not need tobe defined.


toy_story = media.Movie("Toy Story",
                        "a story of a boy and his toys that come to life",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "a marine on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://youtu.be/d1_JBMrrYw8")

pretty_woman=media.Movie("Pretty woman",
                     "a poor girl meets a rich man",
                     "http://www3.pictures.zimbio.com/mp/-VXODjrW5gbx.jpg",
                     "https://youtu.be/Wzii8IuL8lk")

taken = media.Movie("Taken",
                     "A retired CIA agent travels across Europe and relies on his old skills to save his estranged daughter, who has been kidnapped while on a trip to Paris.",
                     "http://stayviolation.typepad.com/.a/6a00d834515bc269e20148c87f21e6970c-pi",
                     "https://youtu.be/uPJVJBm9TPA")


Curse_of_chucky = media.Movie("Curse of chucky",
                     "the story of a doll who comes to live and starts killing people",
                     "https://journalmetrocom.files.wordpress.com/2013/07/chucky.jpg?w=618&h=408&crop=1",
                     "https://youtu.be/lw8rBxYC1Dw")


london_has_fallen = media.Movie("london has fallen",
                     "The american president is being chased around london with his bodyguard",
                     "http://static.rogerebert.com/uploads/movie/movie_poster/london-has-fallen-2016/large_london_has_fallen_ver4_xlg.jpg",
                     "https://youtu.be/3AsOdX7NcJs")

# This is the list of movies that will be fed to the function(open_movies_page) contained within fresh_tomatoes
movies = [toy_story, avatar, pretty_woman,taken,Curse_of_chucky,london_has_fallen]

# This file has a function in it (open_movies_page) which takes in a list of movies as input and returns a webpage that shocase the list of movie given
fresh_tomatoes.open_movies_page(movies)

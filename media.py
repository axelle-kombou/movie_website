import webbrowser
# The class Movie can be think of as a blueprint and it contains data(eg:movie_title...) and method(eg:show_trailer).
class Movie():
# This method is used to initialize (define) all of the data associated to our examples or instances (eg:toy_story).
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube): '''initializing function'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# This method allows the youtube trailer to be displayed on a separate window when we click on the image.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

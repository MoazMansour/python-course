import webbrowser

class Movie():
    def __init__(self,movie_title, movie_storyLine, posterImage, trailer):
        self.title = movie_title
        self.movie_storyLine = movie_storyLine
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailer

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)

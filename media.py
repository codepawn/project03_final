import webbrowser


class Video():

    def __init__(self, movie_title):
        print("Video Called")
        self.title = movie_title


class Movie(Video):

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        print("Movie Called")
        super(Movie, self).__init__(movie_title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    pass


def tester():
    print("goo")

if __name__ == "__main__":
    tester()

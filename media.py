

class Movie:
<<<<<<< HEAD
    """This class holds the information for each movie"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        # title of movie
=======
    def __init__(self, title, poster_image_url, trailer_youtube_url, year='', plot=''):
>>>>>>> b3bececf49efcdb9ad2ed6b6d9d5d51976065189
        self.title = title

        # link to image URL
        self.poster_image_url = poster_image_url

        # link to youtube video url of trailer
        self.trailer_youtube_url = trailer_youtube_url
        self.year = year
        self.plot = plot

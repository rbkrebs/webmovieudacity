import webbrowser


class Movie():

    """This class provides a way to store movie related information.
    This class requires 4 parameters. These parameters must be all strings type.
    It has a construct method to create the instances variables and the show_trailer
    which open a web bronser using webbrowser lib.
    Parameters
    ----------
    movie_title : str
        First parameter. The title of the movie
    movie_storyline : str
        Second parameter. A brief phrase about the movie.
    poster_image : str
        Third parameter. Must be a link (external path) to a imagine related to the movie.
    trailer_youtube : str
        Fourth parameter. Must be a youtube link to the related movie.

    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

        """The constructor of class. It receives 4 strings parameters and create 4 instances variables"""

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):

        """This method use webbrower lib to open a web browser using trailer_youtube_url as parameter"""

        webbrowser.open(self.trailer_youtube_url)

''' Movie class creates a new movie object that
    has a title, poster image, and trailer '''


class Movie():
    ''' Constructor for a movie object.
    Requires a title, poster image, and trailer '''
    def __init__(self, title, box_art, youtube_trailer):
        self.title = title
        self.poster_image_url = box_art
        self.trailer_youtube_url = youtube_trailer

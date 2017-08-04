#!/usr/bin/env python
import webbrowser


class Video:
    """This is a parent class of Movie and TvShow"""

    def __init__(self, title, duration):
        """Inits Video class with title and duration"""
        # print "Video Contruction called"
        self.title = title
        self.duration = duration


class Movie(Video):
    """This class provides a way to store and access movie information"""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']  # class variable

    def __init__(self, movie_title, movie_storyline, poster_image_url, movie_trailer_url, duration):
        """Inits Movie class with title,storyline, image_url, trailer_url, duration"""
        # print "Movie Contructor called"

        Video.__init__(self, movie_title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = movie_trailer_url

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """This class provides a way to store and access movie information"""

    def __init__(self, title, season, episode, tv_station, duration):
        """Inits Tvshow with season, episode, tv station, duration and title"""
        # print "Tv Show constructor called"

        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

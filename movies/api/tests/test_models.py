from django.test import TestCase

from api.models import Movie


class TestMovieModel(TestCase):
    def setUp(self):
        self.movie = Movie(name="Black Panther", year_of_release=2017)
        self.movie.save()

    def test_movie_creation(self):
        self.assertEqual(Movie.objects.count(), 1)

    def test_movie_representation(self):
        self.assertEqual(self.movie.name, str(self.movie))

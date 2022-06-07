from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, Comments, Likes
import datetime

# Create your tests here.
class TestUser(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="ed",email="ed@example.com",password="ed123123")
        self.example_user.save()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.example_user, User))

class TestProfile(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="ed",email="ed@example.com",password="ede43423443")
        self.example_user.save()

        self.example_profile = Profile(user = self.example_user,profile_photo = "./static/images/instahome.png",bio = "The developer", birth_date=datetime.date(1990, 12, 17), location="Westlands")

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.example_profile, Profile))
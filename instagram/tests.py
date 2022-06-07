from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, Comments, Likes
from datetime import date
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
        
        mock_date = date(2021, 3, 4)

        self.example_profile = Profile(user = self.example_user,profile_photo = "./static/images/instahome.png",bio = "The developer", birth_date=mock_date, location="Westlands")

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.example_profile, Profile))

class TestPost(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="ed",email="ed@example.com",password="ede43423443")
        self.example_user.save()

        self.example_profile = Profile(user = self.example_user,profile_photo = "./static/images/instahome.png",bio = "The developer", birth_date=datetime.date(1990, 12, 17), location="Westlands")
        self.example_profile.save()

        self.example_post = Image(image_upload="./static/images/instahome.png",image_name="mypost",image_caption="Lorem ipsum",profile=self.example_profile)

    def tearDown(self) -> None:
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def test_post_instance(self):
        self.assertTrue(isinstance(self.example_post, Image))

    def test_del_instance(self):
        self.example_post.save()
        self.example_post.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

class TestComment(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="ed",email="ed@example.com",password="ede43423443")
        self.example_user.save()

        self.example_profile = Profile(user = self.example_user,profile_photo = "./static/images/instahome.png",bio = "The developer", birth_date=datetime.date(1990, 12, 17), location="Westlands")
       
        self.example_profile.save()

        self.example_post = Image(image_upload="./static/images/instahome.png",image_name="mypost",image_caption="Lorem ipsum",profile=self.example_profile)
        self.example_post.save()

        self.example_comment = Comments(profile=self.example_profile, comment="Nice one", image=self.example_post)

    def tearDown(self) -> None:
        Profile.objects.all().delete()
        Image.objects.all().delete()
        User.objects.all().delete()

    def test_comment_instance(self):
        self.assertTrue(isinstance(self.example_comment, Comments))

    def test_del_comment(self):
        self.example_comment.save()
        self.example_comment.delete()
        self.assertTrue(len(Comments.objects.all())==0)
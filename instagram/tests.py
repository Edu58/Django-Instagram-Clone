from django.test import TestCase
from .models import Profile, Image, Comments, Likes


# Create your tests here.
class TestProfile(TestCase):
    def setUp(self) -> None:
        self.example_category = Profile(user=1, profile_photo='./static/images/instahome.png', bio="This is my bio",
                                        birth_date=2022 - 5 - 17, location='Kagumo')


class TestProfile(TestCase):
    def test_profile(self):
        self.assertTrue(isinstance(self.example_location, Locations))

# class TestImages(TestCase):
#     def setUp(self) -> None:
#         self.example_category = Categories(name="New Category")
#         self.example_category.save()
#
#         self.example_location = Locations(name="Kenya")
#         self.example_location.save()
#
#         self.example_image = Images(name="test image", description="This is a test for the Image model",
#                                     location=self.example_location, category=self.example_category,
#                                     image="../media/images/MG_1684.jpg")
#
#     def tearDown(self) -> None:
#         Categories.objects.all().delete()
#         Locations.objects.all().delete()
#         Images.objects.all().delete()
#
#     def test_image_instance(self):
#         self.assertTrue(isinstance(self.example_image, Images))
#
#     def test_save_image(self):
#         self.example_image.save_image()
#         all_images = Images.objects.all()
#         self.assertTrue(len(all_images) == 1)
#
#     def test_update_image(self):
#         self.example_image.save_image()
#
#         self.updated_category = Categories(name="Gaming")
#         self.updated_category.save()
#         self.updated_location = Locations(name="Kakamega")
#         self.updated_location.save()
#
#         self.example_image.update_image(
#             new_image="../media/images/IMG_6548-4.jpg",
#             new_category=self.updated_category,
#             new_name="New photo",
#             new_location=self.updated_location,
#             new_description="A new photo for testing update image"
#         )
#
#         updated_image = self.example_image
#
#         self.assertEqual(self.example_image, updated_image)
#
#     def test_get_image_by_id(self):
#         self.example_image.save_image()
#         image = self.example_image.get_image_by_id(self.example_image.id)
#         self.assertEqual(self.example_image, image)
#
#     def test_search_image(self):
#         self.example_image.save_image()
#         searched = self.example_image.search_image("New Category")
#         self.assertTrue(len(searched) == 1)
#
#     def test_filter_by_location(self):
#         self.example_image.save_image()
#         searched = self.example_image.filter_by_location("Kenya")
#         self.assertTrue(len(searched) == 1)
#
#     def test_delete_image(self):
#         self.example_image.save_image()
#         self.example_image.delete_image(self.example_image.id)
#         self.assertTrue(len(Images.objects.all()) == 0)

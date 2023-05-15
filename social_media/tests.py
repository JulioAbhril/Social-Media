from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import SocialPost, SocialComment, Image


class SocialPostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='testuser', password='testpass')
        SocialPost.objects.create(
            author=test_user, body='Example text')

    #body post test
    def test_body_content(self):
        post = SocialPost.objects.get(id=1)
        expected_text = f'{post.body}'
        self.assertEquals(expected_text, 'Example text')

    #time post test
    def test_created_on_content(self):
        post = SocialPost.objects.get(id=1)
        self.assertTrue(timezone.now() > post.created_on)

    #author post test
    def test_author_content(self):
        post = SocialPost.objects.get(id=1)
        expected_author = f'{post.author}'
        self.assertEquals(expected_author, 'testuser')


class ImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Image.objects.create()

    def test_image_content(self):
        image = Image.objects.get(id=1)
        example_img = f'{image.image}'
        self.assertEquals(example_img, '')
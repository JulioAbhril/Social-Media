from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # build a user test
        User = get_user_model()
        test_user = User.objects.create_user(username='Abrhiltesteruser', password='12345')
        test_user.save()

           
    def test_profile(self):
        # validate user
        profile = Profile.objects.get(id=1)
        expected_user = f'{profile.user.username}'
        self.assertEquals(expected_user, 'Abrhiltesteruser')
        
        
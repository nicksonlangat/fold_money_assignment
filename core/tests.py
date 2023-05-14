from django.test import TestCase, Client
from accounts.models import UserAccount
from .models import Hashtag, Project


# initialize the APIClient app
client = Client()

class CoreTest(TestCase):

    def setUp(self):
        self.test_user = UserAccount(email='user@user.com', name='user', password='user@8764322wqs')
        self.test_hashtag = Hashtag(name='legacy')
        
        self.test_user0 = UserAccount.objects.create(email='user1@user.com', name='user1', password='user@8764322wqs')
        self.test_hashtag0 = Hashtag.objects.create(name='modern')
        self.test_project = Project(user=self.test_user0, name='awesome',description='this project is awesome')
        self.test_project0 = Project.objects.create(user=self.test_user0, name='new',description='this project is new')
        
    def test_model_can_create_a_user(self):
        old_count = UserAccount.objects.count()
        self.test_user.save()
        new_count = UserAccount.objects.count()
        self.assertNotEqual(old_count, new_count)
    
    def test_model_can_create_a_hashtag(self):
        old_count = Hashtag.objects.count()
        self.test_hashtag.save()
        new_count = Hashtag.objects.count()
        self.assertNotEqual(old_count, new_count)
    
    def test_model_can_create_a_project(self):
        old_count = Project.objects.count()
        self.test_project.save()
        new_count = Project.objects.count()
        self.assertNotEqual(old_count, new_count)
    
    def test_project_string_method(self):
        project = self.test_project0
        expected_string = f'{project.name}'
        self.assertEqual(str(project), expected_string)

    def test_hashtag_string_method(self):
        hashtag = self.test_hashtag0
        expected_string = f'{hashtag.name}'
        self.assertEqual(str(hashtag), expected_string)
    
    def test_user_string_method(self):
        user = self.test_user0
        expected_string = f'{user.email}'
        self.assertEqual(str(user), expected_string)

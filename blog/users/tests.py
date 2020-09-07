from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import Users


# Create your tests here.

class UserTestCase(APITestCase):
    def test_create_user(self):
        print("----------Test to create New User with true format details -------------")
        number_of_user = Users.objects.count()
        mock_user = {
            'name': 'Tester',
            'email': 'tphuoc1998@gmail.com',
            'about_me': 'Im a tester',
        }
        response = self.client.post('/api/users/', mock_user)
        print(response.data)
        print(response.status_code)
        self.assertEqual(Users.objects.count(), number_of_user + 1)
        self.assertEqual(response.data['name'], mock_user['name'])
        print("-----------End of Create User Test------------")

    def test_create_wrong_user_email(self):
        print("----------Test to create New User with wrong Email Format -------------")
        number_of_user = Users.objects.count()
        mock_user = {
            'name': 'Tester',
            'email': '12345',
            'about_me': 'Im a tester',
        }
        response = self.client.post('/api/users/', mock_user)
        print(response.data)
        print(response.status_code)
        self.assertEqual(Users.objects.count(), number_of_user)
        print("-----------End of wrong Email Format Test------------")

    def test_create_blank_user(self):
        print("----------Test to create Blank User -------------")
        number_of_user = Users.objects.count()
        mock_user = {
            'name': '',
            'email': '',
            'about_me': 'Im a tester',
        }
        response = self.client.post('/api/users/', mock_user)
        print(response.data)
        print(response.status_code)
        self.assertEqual(Users.objects.count(), number_of_user)
        print("-----------End of create blank user test------------")

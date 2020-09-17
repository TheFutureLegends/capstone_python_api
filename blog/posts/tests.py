from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Posts


# Create your tests here.

class PostTestCase(APITestCase):
    def test_create_post(self):
        initial_product_count = Posts.objects.count()
        mock_post = {
            'title': 'This is the mocking post',
            'description': 'For capstone project',
            'content': 'testing content',
            'urlToImage': 'https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.learningaboutelectronics.com'
                          '%2FArticles%2FHow-to-create-a-SlugField-in-Django.php&psig=AOvVaw0rNnjBnWoOmDSvxDDNNgYL'
                          '&ust=1599540534846000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOjNzfme1usCFQAAAAAdAAAAABAD',
            'visit': 10,
            'author_id': 1
        }
        response = self.client.post('/api/post/store', mock_post)
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(Posts.objects.count(), initial_product_count + 1)
        for attr, expected_value in mock_post.items():
            self.assertEqual(response.data[attr], expected_value)

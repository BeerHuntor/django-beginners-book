from django.test import TestCase
from django.urls import reverse
from posts.models import Post
# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(post_content="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.post_content, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, "This is a test!")
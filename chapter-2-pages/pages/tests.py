from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageTests(SimpleTestCase):
    # Tests the links to make sure the urls are correct
    def test_url_exits_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    #Tests the names for the links we have designated in URLs.py
    def test_url_available_by_name(self): 
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    #Tests the templates are used correctly and the one we have designated is the correct one
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    
    #Tests the conent of the given template to make sure it matches to what we expect.
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")

class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    #Tests the templates are used correctly and the one we have designated is the correct one
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    
    #Tests the conent of the given template to make sure it matches to what we expect.
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Page</h1>")

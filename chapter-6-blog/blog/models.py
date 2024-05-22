from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    blog_content = models.TextField()


    def __str__(self):
        return f'{self.title}, Writen by {self.author}, Created: {self.date_created}'
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
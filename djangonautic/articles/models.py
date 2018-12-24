from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # Add a thumbnail later
    # add a author later
 
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'



# run these commands after any changes from model
    # python manage.py makemigrations
    # python manage.py migrate

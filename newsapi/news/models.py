from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length = 120)
    description = models.CharField(max_length = 120)
    body = models.TextField()
    location =models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updeted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}{}".format(self.author, self.title)
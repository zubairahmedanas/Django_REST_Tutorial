from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    authorname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

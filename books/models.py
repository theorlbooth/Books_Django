from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title} - {self.author}"

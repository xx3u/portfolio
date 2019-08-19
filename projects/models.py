from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    link = models.CharField(max_length=50)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
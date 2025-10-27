from django.db import models

# Create your models here.
from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_started = models.DateField()
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

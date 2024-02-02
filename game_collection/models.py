from django.db import models

class Genre (models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ManyToManyField("Genre")
    date_of_issue = models.DateField()
    rating = models.DecimalField(decimal_places=1, max_digits=2)

    def __str__(self):
        return self.name

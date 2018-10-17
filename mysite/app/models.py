from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.TextField(null=True)


    def as_json(self):
        return dict(
            name=self.name,
        )


# Create your models here.
class Movie(models.Model):
    name = models.TextField(null=True)
    def as_json(self):
        return dict(
            name=self.name,
        )

# Create your models here.
class MovieToActor(models.Model):
    movie = models.ForeignKey(Movie)
    actor = models.ForeignKey(Actor)

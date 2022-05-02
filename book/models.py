from django.db import models
from config import settings


# Model Mixin
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Origin(TimeStampedModel):
    superhero = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)

    def __str__(self):
        return "{}'s origin: {}".format(self.superhero, self.origin)


class Location(TimeStampedModel):
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return "{}:({},{})".format(self.country, self.latitude, self.longitude)

    class Meta:
        unique_together = ("latitude", "longitude")


class Sighting(TimeStampedModel):
    superhero = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    power = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sighted_on = models.DateTimeField()

    def __str__(self):
        return "{}'s power {} sighted at: {} on {}".format(self.superhero,
                                                           self.power,
                                                           self.location.country,
                                                           self.sighted_on)

    class Meta:
        unique_together = ("superhero", "power")


class Profile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user

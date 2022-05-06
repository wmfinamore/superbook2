from django.db import models
from book.models import TimeStampedModel
from config import settings
from .services import SuperHeroWebAPI
import datetime
from django.utils.functional import cached_property


class BaseProfile(TimeStampedModel):
    USER_TYPES = (
        (0, 'Ordinary'),
        (1, 'SuperHero'),
    )
    birthdate = models.DateField(null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    user_type = models.IntegerField(max_length=1, null=True, choices=USER_TYPES)
    bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "{}: {:.20}".format(self.user, self.bio or "")

    class Meta:
        abstract = True

    @property
    def age(self):
        today = datetime.date.today()
        if self.birthdate:
            return (today.year - self.birthdate.year)-int(
                (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
            )
        else:
            return 0

    # @cached_property
    # def full_name(self):
    #     return self.user.get_full_name()


class SuperHeroProfile(models.Model):
    origin = models.CharField(max_length=100, blank=100, null=True)

    class Meta:
        abstract = True


class OrdinaryProfile(models.Model):
    address = models.CharField(max_length=200, blank=True, Null=True)

    class Meta:
        abstract = True


class Profile(SuperHeroProfile, OrdinaryProfile, BaseProfile):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user

    def is_superhero(self):
        return SuperHeroWebAPI.is_hero(self.user.username)

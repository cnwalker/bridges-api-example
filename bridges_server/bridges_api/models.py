from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    # Extends the native Django user model
    # Look at https://goo.gl/fwZk1w for further explanation
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    # All the following fields should be chosen from a list of valid inputs
    # on the backend and frontend. In this example they're just comma separated
    # strings
    gender = models.CharField(max_length=255, blank=True)
    ethnicity = models.CharField(max_length=255, blank=True)
    disabilities = models.CharField(max_length=255, blank=True)
    current_employer = models.CharField(default="Unemployed", max_length=255, blank=True)

# Receiver is a decorator that activates an action when the native
# django user model has been saved. This lets us create an (empty) UserProfile
# whenever a user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Question(models.Model):
    title = CharField(max_length=300)
    description = TextField(blank=True)
    answer = TextField(blank=True)
    tags = CharField()
    number_of_views = IntegerField()
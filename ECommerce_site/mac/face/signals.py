from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.dispatch import Signal
from .models import Profile


# user_registered = Signal(providing_args=["user", "request"])
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from books.models import Book
import uuid


# Create your models here.
class ProfileManager(models.Manager):
    def get_queryset(self):
        return super(ProfileManager, self).get_queryset().filter(user__is_active=True)


class PatronProfile(models.Model):
    """A profile for users to our application."""

    user = models.OneToOneField(User, related_name='profile')
    library_card_id = models.UUIDField(default=uuid.uuid4, editable=False)
    objects = models.Manager()
    active = ProfileManager()
    borrowed = models.ManyToManyField(Book, related_name='borrowed_by')

    @property
    def is_active(self):
        return self.user.is_active

    def __repr__(self):
        return self.user.username


@receiver(post_save, sender=User)
def make_profile_for_new_user(sender, **kwargs):
    if kwargs['created']:
        new_profile = PatronProfile(
            user=kwargs['instance']
        )
        new_profile.save()

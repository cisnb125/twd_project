from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)      # create a one-to-many relationship with Category
    title = models.CharField(max_length=128)
    url = models.URLField(max_length=200)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    # The upload_to attribute is conjoined with MEDIA_ROOT setting;
    # it will be stored in "tango_with_django_project/media/profile_images."
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
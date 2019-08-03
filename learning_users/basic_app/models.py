from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship
    user = models.OneToOneField(User, on_delete=None)

    # Add any additional attributes
    # blank determines if a field doesn't has to be fielded out
    portfolio = models.URLField(blank=True)

    # Allows user to upload an image to app
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        #Built-in attr of django.contrib.auth.models.User
        # i.e. the User object attr in the 2nd video of level 5
        return self.user.username
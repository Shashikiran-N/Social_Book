from django.db import models

# Create your models here.
class Profile(models.Model):
    user = ""
    id_user = ""
    bio = ""
    profileimg = models.ImageField(upload_to='profile_imagesś', default='default-profile-picture.png')
    location = ""
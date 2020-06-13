from django.db import models

# Create your models here.

class AvatarUpload( models.Model ):
    file = models.FileField(upload_to='avatars/')

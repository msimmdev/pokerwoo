import os
import uuid
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.

def upload_path(instance, filename):
    fn, file_extension = os.path.splitext(filename)
    return 'avatars/{0}{1}'.format(str(uuid.uuid4()), file_extension)

class AvatarUpload(models.Model):
    fs = S3Boto3Storage(bucket='pokerwoo')
    file = models.FileField(upload_to=upload_path, storage=fs)

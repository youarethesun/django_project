import os
from django.db import models
from django.utils import timezone
import random
from django.conf import settings


def portrait_upload_to(instance,filename):
    ext = os.path.splitext(filename)[1]
    fn = '%s_%s%s'% (timezone.now().strftime('%Y%m%d%H%M%S'),
                    random.randint(100000,999999),ext)
    return 'portrait/%s' % fn


PORTRAIT_DEFAULT_PATH = 'images/1.jpg'
class LoginUser(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100,default='嘿')
    portrait = models.ImageField(default='images/1.jpg', upload_to=portrait_upload_to)

    def __str__(self):
        return self.username

    def get_portrait_url(self):
        if not self.portrait:
            return settings.STATIC_URL + PORTRAIT_DEFAULT_PATH
        return self.portrait.url

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import base64

class Tier(models.Model):
    tier_name = models.CharField(max_length=20,unique=True)
    image_presence = models.BooleanField()
    thumbnail_size = models.PositiveIntegerField()
    class Meta:
        unique_together = ("tier_name",)
    def __str__(self):
        return self.tier_name

basic = Tier(tier_name='Basic',image_presence=False,
                  thumbnail_size='200')
premium = Tier(tier_name='Premium',image_presence=True,
                  thumbnail_size='400')
enterprise = Tier(tier_name='Enterprise',image_presence=True,
                  thumbnail_size='400')
try:
    basic.save()
    premium.save()
    enterprise.save()
except:
    pass

class Owner(AbstractUser):
    User = settings.AUTH_USER_MODEL
    status = models.ForeignKey(Tier, null=True,default=1, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        user = super(Owner, self)
        user.set_password(self.password)
        user.save(*args, **kwargs)
        return user

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class UploadImageTest(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField("Image")
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    thumbnail200 = models.URLField(max_length=200, blank=True, null=True)
    thumbnail400 = models.URLField(max_length=200, blank=True, null=True)
    def get_binary(self):
            image_read = bytes(self.image.read())
            binary_image = base64.b64encode(image_read)
            return binary_image


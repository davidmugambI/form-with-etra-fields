from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ZalegoDet(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=30)
    lang = models.CharField(max_length=30)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile '
    # override save method to create profile on save method call
    @receiver(post_save, sender=User)
    def additional_fields(sender, instance, created, **kwargs):
        if created:
            ZalegoDet.objects.create(user=instance)
        instance.zalegodet.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) # save it back to the path

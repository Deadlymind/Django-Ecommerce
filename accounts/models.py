from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Porfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')
    code = models.CharField(default=generate_code, max_length=8)

    def __str__(self):
        return f"{self.user.username}'s Profile"
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Porfile.objects.create(user=instance)


PHONE_TYPE = (
    ('Primary','Primary'),
    ('Secondary','Secondary'),
)


class ContactNumbers(models.Model):
    user = models.ForeignKey(User, related_name='user_contacts',on_delete=models.CASCADE)
    type = models.CharField(max_length=12,choices=PHONE_TYPE)
    number = models.CharField(max_length=20)




ADDRESS_TYPE = [
    ('Home','Home'),
    ('Office','Office'),
    ('Business','Business'),
    ('Other','Other'),
]

class Address(models.Model):
    user = models.ForeignKey(User, related_name='user_address',on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    type = models.CharField(max_length=12,choices=ADDRESS_TYPE)

    def __str__(self):
        return f"{self.user.username}'s {self.get_type_display()} Address"


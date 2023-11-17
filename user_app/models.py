from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


def create_customer(sender, instance, created, **kwargs):
    if created:
        customer_profile = Customer(user=instance)
        customer_profile.save()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpeg')
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    followers = models.ManyToManyField('self', related_name='following')

    def __str__(self):
        return f"{self.user.username}"


post_save.connect(create_customer, sender=User)

from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
MY_CHOICES = ((1, 'Child welfare'),
              (2, 'Education'),
              (3, 'Special needs'),
              (4, 'Healthcare'),
              (5, 'Women welfare'))


# Create your models here.
class BaseUser(AbstractUser):
    is_ngo = models.BooleanField(default=True)
    is_philanthropist = models.BooleanField(default=True)


class Ngo(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='ngo')
    org_name = models.CharField(max_length=100)
    gsn = models.IntegerField()
    primary_cause = MultiSelectField(choices=MY_CHOICES, max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=100)
    certification = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    trust_score = models.FloatField(null=True, default=0)
    fund_received = models.IntegerField(null=True, default=0)
    website_url = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=2000, null=True)
    review_likes = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username


class Philanthropist(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name='philanthropist')
    state = models.CharField(max_length=100)
    primary_cause = MultiSelectField(choices=MY_CHOICES, max_length=200, null=True)
    org_name = models.CharField(max_length=100)
    fund_contrib = models.IntegerField(null=True, default=0)
    phone_number = models.CharField(max_length=100)
    trust_score = models.FloatField(null=True, default=0)

    def __str__(self):
        return self.user.username
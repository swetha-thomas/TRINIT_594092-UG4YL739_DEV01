from django.db import models

from user.models import Ngo

# Create your models here.
class Event(models.Model):
  event_name = models.CharField(max_length=150, null=True, blank=True, default="")
  ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
  event_description = models.TextField()
  funds_raised = models.IntegerField(null=True,default=0)
  funds_required = models.IntegerField(null=True, default=0)
  date = models.DateTimeField(null=True, blank=True)
  perc = models.FloatField(null=True,default=0.0)
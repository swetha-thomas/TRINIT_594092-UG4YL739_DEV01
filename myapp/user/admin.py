from django.contrib import admin
from .models import Ngo, Philanthropist, BaseUser


# Register your models here.
admin.site.register(BaseUser)
admin.site.register(Ngo)
admin.site.register(Philanthropist)

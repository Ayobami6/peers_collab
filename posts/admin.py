from django.contrib import admin
from . models import Posts

# Register your models here.

# adding the models to the admin database
admin.site.register(Posts)

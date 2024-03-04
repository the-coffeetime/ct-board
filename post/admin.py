from django.contrib import admin

# Register your models here.
from .models import Posts, PostFollowers

admin.site.register(Posts)
admin.site.register(PostFollowers)

from django.contrib import admin

# Register your models here.
from .models import Comments, CommentFollowers

admin.site.register(Comments)
admin.site.register(CommentFollowers)
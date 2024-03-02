from django.contrib import admin

# Register your models here.
from .models import Fields, Jobs, Boards, Posts, Comments

admin.site.register(Fields)
admin.site.register(Jobs)
admin.site.register(Boards)
admin.site.register(Posts)
admin.site.register(Comments)
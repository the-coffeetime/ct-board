from django.contrib import admin

# Register your models here.
from .models import Fields, FieldCreationRequest

admin.site.register(Fields)
admin.site.register(FieldCreationRequest)
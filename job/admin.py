from django.contrib import admin

from field.models import Fields
# Register your models here.
from .models import Jobs, JobCreationRequest

admin.site.register(Jobs)
admin.site.register(JobCreationRequest)

from django.contrib import admin

from field.models import Fields
from job.models import Jobs
# Register your models here.
from .models import Boards, BoardCreationRequest

admin.site.register(Boards)
admin.site.register(BoardCreationRequest)

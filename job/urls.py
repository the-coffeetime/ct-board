from django.urls import path

from . import views

# 1. fieldID로 job 목록 조회 - /api/job?fieldID=1
urlpatterns = [
    path('', views.get_jobs, name='getJobs')
]

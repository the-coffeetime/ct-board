from django.urls import path

from . import views

# 1. 모든 field 목록 조회 - /api/field
# 2. fieldID로 field 조회 - /api/field?fieldID=1
urlpatterns = [
    path('', views.get_field, name='getFieldInfo')
]

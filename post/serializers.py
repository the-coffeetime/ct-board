from rest_framework import serializers
from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'  # 모든 필드를 포함하도록 설정
        read_only_fields = ('postID',)  # postID는 자동으로 생성되므로 읽기 전용으로 설정

    def validate(self, data):
        return data

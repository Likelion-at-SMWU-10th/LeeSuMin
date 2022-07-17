from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog # Blog 모델 사용
        fields = ('title', 'pub_date', 'body') # 모든 필드 포함

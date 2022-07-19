from rest_framework import serializers
from blogapp.models import Blog

class BlogSerializer(serializers.ModelSerializer): # 글 작성
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'body')

class BlogListSerializer(serializers.ModelSerializer): # 글 목록 조회
    class Meta:
        model = Blog
        fields = ('id', 'title', 'date', 'summary')
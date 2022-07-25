from rest_framework import serializers
from commentapp.models import Comment

class CommentSerializer(serializers.ModelSerializer): # 댓글 작성
    class Meta:
        model = Comment
        fields = ('id', 'blog', 'content')

class CommentListSerializer(serializers.ModelSerializer): # 댓글 조회
    class Meta:
        model = Comment
        fields = ('id', 'blog', 'content', 'created_at')
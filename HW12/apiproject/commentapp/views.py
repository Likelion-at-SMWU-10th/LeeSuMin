from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CommentSerializer, CommentListSerializer
from .models import Comment

from django.http import Http404

# Create your views here.
class CommentList(APIView):
    def get(self, request): # 모든 댓글 목록 조회하는 경우
        comments = Comment.objects.filter()

        serializer = CommentListSerializer(comments, many=True) # 다수의 쿼리셋 전달 위해서 many = True
        return Response(serializer.data)
    
    def post(self, request): # 댓글 작성하는 경우
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogCommentList(APIView):
    def get(self, request, pk): # 모든 댓글 목록 조회하는 경우
        
        blog_id = request.data['blog']
        print(blog_id)
        comments = Comment.objects.filter(
           blog = blog_id
        )
        serializer = CommentListSerializer(comments, many=True) # 다수의 쿼리셋 전달 위해서 many = True
        return Response(serializer.data)
    

class CommentDetail(APIView):
    def get_object(self, pk): # comment 객체 가져오기
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
    
    def get(self, request, pk): # comment 상세조회
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def put(self, request, pk): # comment 수정
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

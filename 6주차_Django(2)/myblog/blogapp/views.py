from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')

def community(request):
    return render(request, 'blogapp/community.html')

def blog(request):
    blogs = Blog.objects # 모델클래스.objects : 데이터베이스에 저장된 데이터를 '쿼리셋'형태로 반환
    return render(request, 'blogapp/blog.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogapp/detail.html', {'blog': blog_detail})
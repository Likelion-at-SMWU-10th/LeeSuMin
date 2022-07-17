from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import Blog
from .forms import BlogModelForm, CommentForm
from .serializers import BlogSerializer

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')

def blog(request):
    blogs = Blog.objects
    return render(request, 'blogapp/blog.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    form = CommentForm()
    return render(request, 'blogapp/detail.html', {'form': form, 'blog': blog_detail})

def new(request):
    return render(request, 'blogapp/new.html')

def modelformcreate(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogModelForm()
    return render(request, 'blogapp/new.html', {'form': form})

def edit(request):
    return render(request, 'blogapp/edit.html')

def blogupdate(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        form = BlogModelForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('detail', blog_id = post.pk)
    else:
        form = BlogModelForm(instance = post)
        return render(request, 'blogapp/edit.html', {'form': form})

def blogdelete(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    post.delete()
    return redirect('blog')

def result(request):
    query = request.GET.get('query', '') #값이 없으면 빈값으로 대체
    if query:
        blog_objects = Blog.objects.filter(title__contains=query)
        return render(request, 'blogapp/result.html', {'result': blog_objects})
    else:
        return render(request, 'blogapp/result.html', {'error': "검색어를 입력하세요."})

def commentcreate(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            
    return redirect('detail', blog_id=blog.pk)

class BlogListAPI(APIView):
    def get(self, request):
        queryset = Blog.objects.all()
        print(queryset)
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

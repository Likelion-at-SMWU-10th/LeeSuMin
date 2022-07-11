from django.shortcuts import render, redirect, get_list_or_404
from django.utils import timezone

from .models import Diary
from .forms import DiaryForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def calendar(request):
    return render(request, 'calendar.html')

#django form을 이용해서 입력값을 받는 함수
def formcreate(request):
    if request.method == 'POST': # form에 입력한 내용을 db에 저장
        form = DiaryForm(request.POST) 
        if form.is_valid():
            post = Diary()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.date = timezone.now()
            post.save()
            return redirect('/')
    if request.method == 'GET': # 입력받을 수 있는 html 보여주기
        form = DiaryForm()
        return render(request, 'formcreate.html', {'form': form })

def diarylist(request):
    diarys = Diary.objects
    return render(request, 'diarylist.html', {'diarys' : diarys})

'''
def new(request):
    return render(request, 'diaryapp/new.html')

def modelformcreate(request):
    if request.method == 'POST':
        form = DiaryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DiaryModelForm()
    return render(request, 'diaryapp/new.html', {'form' : form})
'''
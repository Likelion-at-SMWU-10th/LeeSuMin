from tracemalloc import get_object_traceback
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.utils import timezone

from .models import Diary
from .forms import DiaryForm, DiaryModelForm

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
            return redirect('diarylist')
    if request.method == 'GET': # 입력받을 수 있는 html 보여주기
        form = DiaryForm()
        return render(request, 'formcreate.html', {'form': form })

def diarylist(request):
    diarys = Diary.objects
    return render(request, 'diarylist.html', {'diarys' : diarys})

def new(request):
    return render(request, 'new.html')

def modelformcreate(request):
    if request.method == 'POST':
        form = DiaryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diarylist')
    else:
        form = DiaryModelForm()
    return render(request, 'new.html', {'form' : form})

def edit(request):
    return render(request, 'edit.html')

def diaryupdate(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    if request.method == 'POST':
        form = DiaryModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('diarylist')
    else:
        form = DiaryModelForm(instance=post)            
        return render(request, 'edit.html', {'form' : form})

def diarydelete(request, diary_id):
    post = get_object_or_404(Diary, pk=diary_id)
    post.delete()
    return redirect('diarylist')

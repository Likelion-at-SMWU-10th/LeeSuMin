from django.shortcuts import render

# Create your views here.

def home(request): #함수 호출하는 것 -> request가 들어오면 request와 home.html화면을 render해준다
    return render(request, 'home.html') 
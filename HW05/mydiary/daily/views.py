from django.shortcuts import render

# Create your views here.
def dailydiary(request):
    return render(request, 'dailydiary.html')

def showdiary(request):
    return render(request, 'showdiary.html')
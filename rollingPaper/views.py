from django.http import request
from django.shortcuts import render
from .models import Comment

def main(request):
    return render(request, 'rollingPaper_main.html')

def postit(request):
    comments = Comment.objects.all() #Blog 테이블에 있는 오브젝트 모두를 불러오기.
    return render(request, 'postitPage.html', {'comments':comments}) #home.html 과 함께 blogs를 보내준다.

def add_post(request):
    return render(request, 'post.html')

def form_rolling(request):
    return render(request, 'rollingPaper_form.html')

def code_rolling(request):
    return render(request, 'rollingPaper_code.html')



from django.shortcuts import render
from .models import Comment

def postit(request):
    comments = Comment.objects.all() #Blog 테이블에 있는 오브젝트 모두를 불러오기.
    print("함수 실행");
    return render(request, 'postitPage.html', {'comments':comments}) #home.html 과 함께 blogs를 보내준다.

    
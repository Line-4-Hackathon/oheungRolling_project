from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib import messages
import uuid
import base64
from .models import RollingInfo
from .models import Comment
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.dateformat import DateFormat
from .models import Comment


def postit(request):
    comments = Comment.objects.all() #Blog 테이블에 있는 오브젝트 모두를 불러오기.
    return render(request, 'postitPage.html', {'comments':comments}) #home.html 과 함께 blogs를 보내준다.

def add_post(request):
    return render(request, 'post.html')

def form_rolling(request):
    return render(request, 'rollingPaper_form.html')

def code_rolling(request):
    return render(request, 'rollingPaper_code.html')

# Create your views here.


#main 페이지를 띄워주는 함수
def main(request):
    return render(request, "main.html")


#코드 확인해주는 함수, 일치하는 코드가 없다면 경고창 띄움, 일치하는 코드가 있다면 <<일치하는 코드의 페이지>>로 연결
'''
def codeconfirm(request, rollings_id):
    my_roll = RollingInfo.objects.get(pk=rollings_id)
    if request.method == 'POST' :
        rolling_id = request.POST.get('rolling_id') #안되면 get 지우기
        confirm = authenticate(rolling_id=rolling_id)
    
        if confirm is None:
            messages.error(request, "Code is not exist !", 
                            extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, '/detail/'+str(my_roll.pk))'''

'''
def codeconfirm(request):
    my_roll = RollingInfo.objects.get(pk=roll_id)
    if request.method == 'POST' :
        roll_id = request.POST.get('codeinput') #안되면 get 지우기
        confirm = authenticate(roll_id=roll_id)
    
        if confirm is None:
            messages.error(request, "Code is not exist !", 
                            extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, '/detail/'+str(my_roll.pk))
'''
'''
#롤링페이퍼 만들어주는 함수
def creat_rolling(request):
    form = CreateForm()
    if request.method == 'POST' :
        form = CreateForm(request.POST, request.FILES)'''


#랜덤 코드를 생성해주는 함수 
'''
def random_code(length=6):
    """
    generates random code of given length
    """
    code = base64.urlsafe_b64encode(
    	uuid.uuid4().bytes.encode("base64").rstrip()
    ).decode()[:length]
    
    #rolling_detail = get_object_or_404(RollingInfo, pk=rolling_id)
    return render(request, 'detail.html', {'code':code})'''
'''

#롤링페이퍼 아이디에 맞는 페이지를 보여준다.
def detail(request, rolling_id):
    rolling_detail = get_object_or_404(RollingInfo, pk=rolling_id)
    return render(request, 'detail.html', {'rolling': rolling_detail})
    
'''
#데드라인이 넘으면
def deadline(request):
    today = datetime.today().strftime("%Y%m%d")
    today = int(today)
    rollings = RollingInfo.objects.all()
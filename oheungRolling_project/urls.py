"""oheungRolling_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rollingPaper import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    # path('detail/<str:id>', views.detail, name='detail'),
    # path("codeconfirm", views.codeconfirm, name='codeconfirm'),
    # path('admin/', admin.site.urls),
    path('postit/', views.postit, name = "postit"),
    path('form/', views.form_rolling, name = "form"),
    path('add_post/', views.add_post, name ="add_post"),
    path('random_code/', views.generate_random_code, name = "random_code"),
    path('create', views.create, name = "create"),
]

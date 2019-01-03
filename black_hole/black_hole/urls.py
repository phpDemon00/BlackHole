"""black_hole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from mini_hole import views            #import my views

from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse


def my_func(request):
	return HttpResponse("Hello Hello")

urlpatterns = [
	
    path('admin/', admin.site.urls),
    #simple url
    path('mini/', views.test_index, name='index'),
    path('mypage/', my_func,),

    #templates url
    path('',views.func_rend,),
    path('next_page/',views.next_page,),
    
]








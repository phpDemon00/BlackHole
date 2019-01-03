from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def test_index(request):
    return HttpResponse("Hello, world. You're at the mini_hole index.")

def func_rend(request):
	print(request.GET)
	print(request.POST)
	return render(request, "index.html",)

def next_page(request):
	return render(request, "next_page.html",)

# def index(request):
# 	return render(request, "black_hole/index.html",{})
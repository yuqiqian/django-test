from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse('Hello this is index page')

def home(request):
	string = "I'm learning django!"
	testList = ["HTML", "CSS", "jQuery", "Python", "Django"]
	testDict = {"site":"myOwnSite", "content":"Hello, welcome to my site!"}
	testList2 = map(str, range(100))
	return render(request, 'home.html', {"List" : testList2})
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
#create home function to manage resquests
#create list

def home(request):
	#create disctionary
	context ={
	    'posts':Post.objects.all(),
	    'title':'Home'
	}
	return render(request,'blog/home.html',context)
	
def about(request):
	return render(request,'blog/about.html',{'title':'about'})
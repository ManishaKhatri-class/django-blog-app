from django.shortcuts import render
from django.http import HttpResponse

#create home function to manage resquests
#create list
posts =[

  {
	'author' :'CoreyMS',
	'post_title' : 'Blog Post 1',
	'content' : 'First post content',
	'date_posted' : 'August 27 , 2018'
  },
  {
	'author' :'Jane Doe',
	'post_title' : 'Blog Post 2',
	'content' : 'Second post content',
	'date_posted' : 'October 26 , 2019'
  },
 

]
def home(request):
	#create disctionary
	context ={
	    'posts':posts,
	    'title':'Home'
	}
	return render(request,'blog/home.html',context)
	
def about(request):
	return render(request,'blog/about.html',{'title':'about'})
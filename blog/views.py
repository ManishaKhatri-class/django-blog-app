from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
#create home function to manage resquests
#create list

def home(request):
	#create disctionary
	context ={
	    'posts':Post.objects.all(),
	    'title':'Home'
	}
	return render(request,'blog/home.html',context)
class PostListView(ListView):
	model =Post
	template_name='blog/home.html'#create post_list.html in templates in views.py 
	context_object_name='posts'
	ordering=['-date_posted']#sort posts
	
class PostDetailView(DetailView):
	model =Post
	
class PostCreateView(LoginRequiredMixin,CreateView):
#mixin so only user of blog shoes post is can only update his post
	model =Post
	fields=['title','content']
	#create currently loginned user the author
	def form_valid(self,form):
		form.instance.author=self.request.user 
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model =Post
	fields=['title','content']
	#create currently loginned user the author
	def form_valid(self,form):
		form.instance.author=self.request.user 
		return super().form_valid(form)
	def test_func(self):
		post=self.get_object()
		if self.request.user ==post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model =Post
	success_url=reverse_lazy('blog-home')#redirect back to home page
	def test_func(self):
		post=self.get_object()
		if self.request.user ==post.author:
			return True
		return False


def about(request):
	return render(request,'blog/about.html',{'title':'about'})
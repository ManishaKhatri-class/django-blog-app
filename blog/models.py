from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)#auto_now_add=True when we need only date when post is posted , default=timezone.now when we ant to chnage dtae modified
	author=models.ForeignKey(User,on_delete=models.CASCADE)#when we want unique author for his post and also delete post when author deleted
def __str__(self):
	return self.title
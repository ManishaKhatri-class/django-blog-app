from django.db import models

from django.contrib.auth.models import User

class Donation(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	razorpay_order_id=models.CharField(max_length=100)
	razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
	razorpay_signature=models.CharField(max_length=255,blank=True,null=True)
	amount=models.IntegerField()
	status=models.CharField(max_length=20,default='created')
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} -{self.amount/100} INR -{self.status}"



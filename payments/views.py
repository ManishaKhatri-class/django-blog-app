from django.shortcuts import render

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import razorpay
from .models import Donation

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@login_required
def donate_page(request):
	return render(request,"payments/donate.html")

@login_required
def create_donation_order(request):
	amount=int(request.GET.get("amount",0))*100 #amount in paise
	if amount< 100:
		return JsonResponse({"error": "Enter Valid Amount"},status=400)

	order=client.order.create({
		"amount":amount,
		"currency":"INR",
		"payment_capture":1
		})	
	#save order in db
	donation =Donation.objects.create(
		user=request.user,
		razorpay_order_id=order['id'],
		amount=amount
		)
	return JsonResponse({

		"order_id":order['id'],
		"amount":amount,
		"currency":"INR",
		"key":settings.RAZORPAY_KEY_ID
		})
@csrf_exempt
def verify_donation(request):
	if request.method=="POST":
		data=request.POST
		razorpay_order_id=data.get("razorpay_order_id")
		razorpay_payment_id=data.get("razorpay_payment_id")
		razorpay_signature=data.get("razorpay_signature")

		donation=Donation.objects.get(razorpay_order_id=razorpay_order_id)

		params_dict={
		'razorpay_order_id':razorpay_order_id,
		'razorpay_payment_id':razorpay_payment_id,
		'razorpay_signature':razorpay_signature
		}
		#verify payment signature
		try:
			client.utility.verify_payment_signature(params_dict)
			donation.razorpay_payment_id=razorpay_payment_id
			donation.razorpay_signature=razorpay_signature
			donation.status="paid"
			donation.save()
			return JsonResponse({"status":"Payment Verified"})
		except:
			donation.status="Failed"
			donation.save()
			return JsonResponse({"status":"Payment Verification Failed"},status=400)

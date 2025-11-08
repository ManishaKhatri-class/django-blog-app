from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail
import Mail
from django.conf import settings
 def send_mail(to_email,subject,html_content):
 	message=Mail(
            subject="Password Reset Request",
            message='Hi,click the link below to reset your password',
 		from_email=settings.DEFAULT_FROM_EMAIL,
 		recipient_list=[user.email],
 		)
 	try:
 		sg=SendGridAPIClient(settings.SENDGRID_API_KEY)
 		response=sg.send(message)
 		print(response.status_code)
 		print(response.body)
 		print(response.headers)
		return True
	except Exception as e:
		print("Error sending email",str(e))
		return False
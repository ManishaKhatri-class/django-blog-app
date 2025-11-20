from django.urls import path
from . import views

urlpatterns = [
    path("donate/", views.donate_page, name="donate_page"),
    path("create-order/", views.create_donation_order, name="create_donation_order"),
    path("verify/", views.verify_donation, name="verify_donation"),
]

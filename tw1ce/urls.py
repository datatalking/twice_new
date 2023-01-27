from django.urls import path

from tw1ce import views

urlpatterns = [

    path('', views.homepage, name="homepage"),
    path('pricing', views.pricing, name="pricing"),
    path('faq', views.faq, name="faq"),
    path('contact', views.contact, name="contact"),
    path('privacy-and-policy', views.legal, name="legal"),
    path('login', views.login, name="login"),
    path('registration', views.registration, name="registration"),


]


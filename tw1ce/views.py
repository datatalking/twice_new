from django.shortcuts import render

# Create your views here.


def homepage(request):

    return render(request, 'main/home_page.html')

def pricing(request):
    return render(request, 'main/pricing_page.html')


def faq(request):
    return render(request, 'main/faq_page.html')


def contact(request):
    return render(request, 'main/contact_page.html')


def legal(request):
    return render(request, 'main/legal_page.html')


def login(request):
    return render(request, 'main/login_page.html')


def registration(request):
    return render(request, 'main/signup_page.html')
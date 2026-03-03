# email_sender/views.py
from django.shortcuts import render,redirect
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse
from .utils import send_mail
from bulk_email.models import *

stripe.api_key = settings.STRIPE_SECRET_KEY

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        occupation = request.POST.get('occupation')
        password = request.POST.get('password')

        user = Signup_user(
            name = full_name,
            email=email,
            phone_number = phone_number,
            occupation = occupation,
            password = password
        )
        user.save()
        return HttpResponse("Signup success")


    return render(request, "signup.html")

def home(request):
    content = Card_text_all.objects.first()
    home_head = Home_head.objects.first()
    footer = Footer.objects.first()
    pricing = Pricing.objects.first()
    return render(request, "index.html", {"content":content,"head":home_head,"footer":footer,"pricing":pricing})

def dash(request):
    if request.method == 'POST':
        file_name = request.FILES['file']
        subject = request.POST.get('subject')
        message = request.POST.get('message')   
        send_mail(file_name, subject, message)
        return render(request, 'success.html')
    
    return render(request, "email_form.html")

def pricing(request):
    footer = Footer.objects.first()
    if request.method == 'POST':
        Pricing.objects.all().delete()
        price1 = request.POST.get('price1')
        price2 = request.POST.get('price2')
        price3 = request.POST.get('price3')
        Pricing.objects.create(price1=price1, price2=price2, price3=price3)
        
    content = Pricing.objects.first()
    return render(request, "pricing.html", {"content": content,"footer":footer})

def process_payment(request):
    if request.method == 'POST':
        cardholder_name = request.POST.get('cardholder_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvc = request.POST.get('cvc')

        try:
            # Create a Stripe token
            token = stripe.Token.create(
                card={
                    "number": card_number,
                    "exp_month": expiry_date.split('/')[0],
                    "exp_year": expiry_date.split('/')[1],
                    "cvc": cvc,
                },
            )

            # Process payment using the token
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency='usd',
                source=token.id,
                description='Example charge',
            )

            # Payment success
            return JsonResponse({'success': True})

        except stripe.error.CardError as e:
            # Payment failed
            return JsonResponse({'success': False, 'error_message': str(e)})
    return render(request,"payment.html")

# def footer(request):
#     foot = Footer.objects.first()
#     return render(request,"footer.html",{"footer":foot})
from django.contrib import admin
from django.urls import path
from bulk_email import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home, name="home"),
    path('dashboard',views.dash, name="dashboard"),
    path("pricing",views.pricing, name= "pricing"),
    path("signup",views.signup, name="signup"),
    path('process_payment/', views.process_payment, name='process_payment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
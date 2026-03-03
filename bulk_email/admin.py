from django.contrib import admin
from .models import *

# Register your models here.


class Signup_view(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Card_text_all)
admin.site.register(Pricing)
admin.site.register(Home_head)
admin.site.register(Footer)
admin.site.register(Signup_user,Signup_view)
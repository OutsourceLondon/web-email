from django.db import models

# Create your models here.
class Signup_user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Card_text_all(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.TextField()
    title2 = models.CharField(max_length=100)
    description2 = models.TextField()
    title3 = models.CharField(max_length=100)
    description3 = models.TextField()
    def __str__(self):
        return self.title1

class Pricing(models.Model):
    home_price1 = models.CharField(max_length=100)
    home_price2 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    c1t1 = models.CharField(max_length=100)
    c1t2 = models.CharField(max_length=100)
    c1t3 = models.CharField(max_length=100)
    c2t1 = models.CharField(max_length=100)
    c2t2 = models.CharField(max_length=100)
    c2t3 = models.CharField(max_length=100)
    c2t4 = models.CharField(max_length=100)
    c3t1 = models.CharField(max_length=100)
    c3t2 = models.CharField(max_length=100)
    c3t3 = models.CharField(max_length=100)
    c3t4 = models.CharField(max_length=100)
    def __str__(self):
        return self.price1
    
class Home_head(models.Model):
    head = models.CharField(max_length=100)
    text1 = models.CharField(max_length=100)
    text2 = models.CharField(max_length=100)
    def __str__(self):
        return self.head
    
class Footer(models.Model):
    logo_text = models.TextField()
    cat1_title = models.CharField(max_length=100)
    cat1_text1 = models.CharField(max_length=100)
    cat1_text2 = models.CharField(max_length=100)
    cat1_text3 = models.CharField(max_length=100)
    cat1_text4 = models.CharField(max_length=100)
    cat2_title = models.CharField(max_length=100)
    cat2_text1 = models.CharField(max_length=100)
    cat2_text3 = models.CharField(max_length=100)
    cat2_text4 = models.CharField(max_length=100)
    cat2_text5 = models.CharField(max_length=100)
    cat3_title = models.CharField(max_length=100)
    cat3_text1 = models.CharField(max_length=100)
    cat3_text2 = models.CharField(max_length=100)
    cat3_text3 = models.CharField(max_length=100)
    cat3_text4 = models.CharField(max_length=100)
    cat4_title = models.CharField(max_length=100)
    cat4_text1 = models.CharField(max_length=100)
    cat4_text2 = models.CharField(max_length=100)
    cat4_text3 = models.CharField(max_length=100)
    cat4_text4 = models.CharField(max_length=100)



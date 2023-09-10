from django.db import models

# Create your models here.
class floods(models.Model):
    Camp_id=models.CharField(max_length=6)
    Camp_Name=models.CharField(max_length=35)
    Name=models.CharField(max_length=540)
    Mailid=models.CharField(max_length=140)
    Password=models.CharField(max_length=100)
    Camp_address=models.CharField(max_length=300)
    District=models.CharField(max_length=100)
    State=models.CharField(max_length=140)
    Country=models.CharField(max_length=140)
    Pincode=models.IntegerField()
    img=models.ImageField(upload_to="pics")
    Total_noof_capacity=models.CharField(max_length=140)
class form(models.Model):
     Camp_Id=models.CharField(max_length=6)
     Name=models.CharField(max_length=36)
     Age=models.IntegerField()
     Gender=models.CharField( max_length=32)
     Address=models.CharField(max_length=45)
     Contact=models.IntegerField()
   
class regist(models.Model):
    Camp_Id=models.CharField(max_length=6)
    
    Product=models.CharField( max_length=32)
    Quantity=models.CharField( max_length=32)
     
     
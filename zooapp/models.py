from django.db import models

# Create your models here.
class Registration(models.Model):
    Type = (
        ('male','male'),
        ('female','female'),
        ('other','other')
    )
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=30,choices=Type)
    contact_number = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)
    
    def __str__(self):
        return self.email
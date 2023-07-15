from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('HM', 'Hospital Manager'),
        ('GU', 'Guest'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_hospital=models.BooleanField(default=False)
    # Add any additional fields or methods you need

    def __str__(self):
        return self.username
    

class Hospital(models.Model):

    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        "core.User",
        on_delete=models.CASCADE,
        null=True
    )
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='hospital_images',blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class HospitalImage(models.Model):
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
    )
    imagefile = models.ImageField(upload_to='hospital_images',blank=True,)
    def __str__(self):
        return self.hospital.name

class HospitalVideo(models.Model):
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
    )
    videofile = models.FileField(upload_to='hospital_videos')
   

    def __str__(self):
        return self.hospital.name
    
class Service(models.Model):
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    detail = models.TextField(max_length=1000)
    
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):

    Gender_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    hospital = models.ForeignKey(
            'Hospital',
            on_delete=models.CASCADE,
        )
    first_name = models.CharField(max_length=255,default=None)
    last_name = models.CharField(max_length=255,default=None)
    age = models.IntegerField()
    service_id = models.ForeignKey(
            'Service',
            on_delete=models.CASCADE,
        )
    created_by=models.ForeignKey(
            "core.User",
            on_delete=models.CASCADE,default=None
        )
    gender = models.CharField(max_length=10 ,choices=Gender_CHOICES)
    created_time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.hospital.name,self.name
    
class Comment(models.Model):
    email = models.CharField(max_length=255)
    comment=models.TextField(max_length=2000)
    hospital=models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.email
    


from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
import string, random

# UUID Creation for Property model
def gen_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

# Create your models here.
class Tenant(models.Model):
    Tenant_firstName = models.CharField(max_length=32)
    Tenant_lastName = models.CharField(max_length=32)
    Tenant_Email = models.EmailField(unique=True, null=True)
    Tenant_Phone = PhoneNumberField(unique=True, null=True, blank=True)


class Property(models.Model):
    Property_code = models.UUIDField(default=gen_code, editable=False, unique=True, max_length=8)
    Property_name = models.TextField()
    Property_roomNum = models.IntegerField()


class Room(models.Model):
    Room_isOccupied = models.BooleanField(default=False)
    Room_image = models.ImageField(upload_to='assets', default='assets/test1.png')
    Room_tenant = models.CharField(max_length=128, default='Tenant')


class Reports(models.Model):    
    Reports_header = models.TextField()
    Reports_body = models.TextField()
    Reports_author = models.CharField(max_length=128)
    Reports_isCompleted = models.BooleanField(default=False)


class Announcements(models.Model):
    Announce_header = models.CharField(max_length=100)
    Announce_body = models.TextField()
    Announce_image = models.ImageField(upload_to='announcements/', blank=True, null=True)
    Announce_date = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return self.Announce_header

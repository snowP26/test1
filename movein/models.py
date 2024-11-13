from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    )

    role = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='tenant')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and not self.role:
            self.role = 'tenant' 
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# UUID Creation for Property model
def gen_code():
    return str(uuid.uuid4())[:8]

class Property(models.Model):
    # Proprty identification
    Property_code = models.CharField(default=gen_code, editable=False, unique=True, max_length=8)
    Property_ownerId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='property')
    Property_image = models.ImageField(upload_to='assets/properties', default='assets/test1.png')

    # Property information
    Property_name = models.TextField()
    Property_roomCount = models.IntegerField()


class Room(models.Model):
    # Room information
    Room_isOccupied = models.BooleanField(default=False)
    Room_image = models.ImageField(upload_to='assets/rooms', default='assets/test1.png')

    # Room identification
    Room_Code = models.CharField(default=gen_code, editable=False, unique=True, max_length=8)
    Room_propertyId = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='room')


class Reports(models.Model):    
    # Report Information
    Reports_header = models.TextField()
    Reports_body = models.TextField()
    Reports_isCompleted = models.BooleanField(default=False)
    Reports_date = models.DateTimeField(default=timezone.now)

    # Report Identification
    Reports_authorId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')


class Announcements(models.Model):
    # Report information
    Announce_header = models.CharField(max_length=100)
    Announce_body = models.TextField()
    Announce_date = models.DateTimeField(default=timezone.now)

    # Report identification
    Announce_authorId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcements')

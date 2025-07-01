from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Common model for tracking created info
class TimeStampedModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('regular', 'Regular Staff'),
        ('admin', 'Administrative Staff'),
        ('super', 'System Administrator'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='regular')
    contact = models.CharField(max_length=20, blank=True)
    profile_pic = models.ImageField(upload_to='user_profiles/', blank=True, null=True)


    def __str__(self):
        return f"{self.user.username} ({self.role})"


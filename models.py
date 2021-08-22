from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

class UserProfile(AbstractUser):
    usertype=models.CharField(max_length=50)


DEMO_CHOICES =(
    ("Selected","Selected"),
    ("Selected for Next Round","Selected for Next Round"),
    ("Rejected", "Rejected"),
    ("No Update", "No Update"),
)
REC = (
    ("Yes", "Yes"),
    ("No", "No"),
    
)

class AddInt(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE, blank=True, null=True)
    c_name=models.CharField(verbose_name='Company Name',null=True,max_length=30, blank=True)
    c_url=models.CharField(verbose_name='Company URL',null=True,max_length=30, blank=True)
    c_contact=models.IntegerField(verbose_name='Company Contact',null=True,blank=True)
    c_post=models.CharField(verbose_name='Post Applied',null=True,max_length=40, blank=True)
    c_email=models.EmailField(verbose_name='Company Email',null=True, blank=True)
    date_applied=models.DateField(null=True,blank=True)
    scd_date=models.DateField(null=True,blank=True)
    rec_called=models.CharField(verbose_name='Did the Reruiter Call',null=True,max_length=20,choices=REC, blank=True)
    int_rounds_cleared=models.IntegerField(verbose_name='Interview Rounds Cleared',null=True,blank=True)
    que_asked=models.TextField(verbose_name='Questions Asked',null=True, blank=True,max_length=50)
    self_analysis=models.TextField(verbose_name='Self Analysis',null=True, blank=True,max_length=50)
    resp_status=models.CharField(verbose_name='Response Status',null=True,max_length=30,choices=DEMO_CHOICES, blank=True) 

    def less_than_one_day(self):
        return (self.scd_date - datetime.date.today()).days == 1

    def more_than_one_day(self):
        return (self.scd_date - datetime.date.today()).days > 1

    def int_date(self):
        return (datetime.date.today() - self.scd_date).days == 0

    def past_date(self):
        return (self.scd_date < datetime.date.today())
    

    class Meta:
        db_table='interview_tracker'


class Notes(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE, blank=True, null=True,)
    note_name=models.CharField(max_length=20)
    note_content=models.TextField(max_length=128)
    note_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'note_maker'
       

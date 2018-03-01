from django.contrib.auth.models import Permission, User
from django.db import models

# this table for Organization in heir user is reprent id which default value is 1
class Organization(models.Model):
    user = models.ForeignKey(User, default=1)
    established = models.CharField(max_length=250)
    organization_name = models.CharField(max_length=500)
    organization_type = models.CharField(max_length=100)
    organization_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.organization_name + ' - ' + self.established

 # this is another table where many event information attach their 
class Special_event(models.Model):
    # in here organization is connect with another Organization table 
    # with ForeignKey key this is most important part of database design
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date = models.CharField(max_length=500)
    time =models.CharField(max_length=200)
    topic = models.CharField(max_length=20000)
    location = models.CharField(max_length=500)
    event_detail = models.CharField(max_length=500)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.topic + '-'+ self.time + '-'+ self.location


# model.py  is mainly use for organize a table structure on that occasion 
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created"]

class Note(TimeStampedModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='note_user')
    title = models.CharField(max_length=255)
    text = models.TextField(null=True,blank=True)
    media = models.FileField(null=True,blank=True)

class SharedNote(TimeStampedModel):
    note = models.ForeignKey(Note,on_delete=models.CASCADE,related_name='shared_note')
    receiver = models.ForeignKey(User,on_delete=models.SET_NULL,related_name='receiver_user',null=True,blank=True)

from django.db import models
from django.utils import timezone

# Create your models here.

class Status(models.Model):
    status_id = models.IntegerField(unique=True)
    status = models.CharField(max_length=255)
    member = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True, blank=True, related_name='status_records')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.status_id} - {self.status}"
    
    class Meta:
        ordering = ['status_id']


class Member(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    status=models.CharField(max_length=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
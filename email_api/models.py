from django.db import models
from  django.contrib.auth.models import User

class EmailBox(models.Model):
    sender = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    from_email = models.EmailField(max_length=100, null=True, blank=True)
    to_email = models.EmailField(max_length=100)
    email_subject = models.CharField(max_length=100)
    email_body = models.TextField(max_length=500)

    def __str__(self):
        return self.email_subject
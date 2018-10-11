from django.db import models

class Email(models.Model):
    from_email = models.EmailField(max_length=100, null=True, blank=True)
    to_email = models.EmailField(max_length=100)
    email_subject = models.CharField(max_length=100)
    email_body = models.TextField(max_length=500)


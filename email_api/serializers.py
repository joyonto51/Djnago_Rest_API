from rest_framework import serializers
from .models import Email

class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['to_email','email_subject','email_body']
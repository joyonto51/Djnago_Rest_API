from rest_framework import serializers
from .models import EmailBox

class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailBox
        fields = ['to_email','email_subject','email_body']
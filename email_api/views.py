import sendgrid
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from sendgrid.helpers.mail import *
from django.views import View


class EmailSendView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'email.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('text')

        sg = sendgrid.SendGridAPIClient(apikey='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')
        from_email = Email("aarosh.itsd@gmail.com")
        to_email = Email(email)

        content = Content("text/plain", text)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())

        print(response.status_code)
        print(response.body)
        print(response.headers)

        return HttpResponseRedirect(reverse('email'))
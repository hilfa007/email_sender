from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
from django.http import Http404, HttpResponseBadRequest
from django.http import JsonResponse
from django.core import serializers
from rest_framework import status

from rest_framework import generics
from rest_framework import viewsets

from django.http import HttpResponse
import traceback
from django.core.mail import send_mail
from django.template import loader


def index(request):
    html_message = loader.render_to_string(
        'message.html',
        {
            'name': 'Recipient Name',
            'body': 'This email is to verify whether we can send email in Django from Gmail account.',
            'sign': 'Sender',
        })
    send_mail(
        'Congratulations!',
        'You are lucky to receive this mail.',
        'from@example.com',
        ['to@example.com'],
        html_message=html_message,
        fail_silently=False,
    )

    return HttpResponse("Mail Sent!!")
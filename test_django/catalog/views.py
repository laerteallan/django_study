from django.shortcuts import render
from django.http import  JsonResponse
# Create your views here.
#
import json

from django.http import  HttpResponse

response_data = {}
response_data['result'] = 'laerte allan'
response_data['message'] = 'teste'



def test_view(request):


    return JsonResponse(response_data, status=500)

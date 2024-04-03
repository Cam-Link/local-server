from django.shortcuts import render
from camlink.models import Link

import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def start():
  pass







def link():
  pass







def stream():
  pass






def refresh():
  pass





def play():
  pass








@csrf_exempt
def stop(request):
  try:   

    if request.method == "GET":
      try:
        
        links = Link.objects.all()

        links.delete()

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})
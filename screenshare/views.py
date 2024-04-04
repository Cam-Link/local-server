from django.shortcuts import render

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







@csrf_exempt
def play(request):
  try:   

    if request.method == "GET":
      try:
        
        num = request.session.get("num",0)

        

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})

  except:
    return JsonResponse({'msg':"Unexpected error"})







def stop():
  pass
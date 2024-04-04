from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

code = ""
number = 0


@csrf_exempt
def start(request):
  global code

  try:   

    if request.method == "POST":
      try:
        
        code = "screen"

        return JsonResponse({'msg':'success','code':code})

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})








def link():
  pass







def stream():
  pass








def play():
  pass







def stop():
  pass

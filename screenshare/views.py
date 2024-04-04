from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def start():
  pass







@csrf_exempt
def link(request):
  global code

  try:   

    if request.method == "POST":
      try:
        
        data = json.loads(request.body)['code']

        if data != code:
          return JsonResponse({'msg':'code does not match'})

        request.session['num'] = 0

        return JsonResponse({'msg':'success'})

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})

  except:
    return JsonResponse({'msg':"Unexpected error"})








def stream():
  pass








def play():
  pass







def stop():
  pass
from django.shortcuts import render

import os
import json
from django.http import JsonResponse, FileResponse
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




@csrf_exempt
def play(request):
  try:   

    if request.method == "GET":
      try:
          
        data = json.loads(request.body)

        uid = data['uid']
        cid = data['cid']

        #return the requested chunk of video
        
        
        path = os.getcwd() + f"/camlink/videos/{uid}/{cid}.webm"

        chunk = open(path, 'rb')

        return FileResponse(chunk, content_type='video/webm')

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})
from django.shortcuts import render
from camlink.models import Link

import os
import shutil
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

    if request.method == "POST":
      try:
        
        #clear the database

        links = Link.objects.all()

        links.delete()

        #move the recordings to exports folder

        current_dir = os.getcwd()
        videos_dir = current_dir + "/camlink/videos"
        exports_dir = current_dir + "/camlink/exports"

        folders = os.listdir(videos_dir)

        for i in folders:
          path = videos_dir + "/" + i + "/full/"
          file = os.listdir(path)[0]

          source = path + file
          destination = exports_dir + "/" + file

          os.rename(source, destination)


        #delete the folders inside the videos folder

        for i in folders:
          shutil.rmtree(videos_dir + "/" + i)


        return JsonResponse({'msg':"message"})

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})
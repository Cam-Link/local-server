from django.shortcuts import render

import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from camlink.models import Link

# Create your views here.


def start():
  pass






@csrf_exempt
def link(request):
  try:   

    if request.method == "POST":
      try:
          
        data = json.loads(request.body)

        code = data['code']

        #return error message if the code doesn't match with the code variable here

        #create a new link or user in the model

        new_link = Link()

        new_link.save()

        id = new_link.id

        #save the id in session to be sent as cookie

        request.session['uid'] = id

        #create the directories which belong to the new user

        os.makedirs(f"camlink/videos/{id}/full")

        

        return JsonResponse({'msg':'message'})

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})







def stream():
  pass






def refresh():
  pass





def play():
  pass
from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from camlink.models import Link

# Create your views here.


def start():
  pass







def link(request):
  try:   

    if request.method == "POST":
      try:
          
        data = json.loads(request.body)

        code = data['code']

        #return error message if the code doesn't match with the code variable here

        new_link = Link()

        new_link.save()

        request.session['uid'] = new_link.id

        

        return JsonResponse(data)

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
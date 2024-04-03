from django.shortcuts import render
from camlink.models import Link

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
def refresh(request):
  try:   

    if request.method == "GET":
      try:
        
        peers = int(request.session.get("peers",0))

        last_id = int(Link.objects.all().order_by('-id')[0].id)

        if peers == last_id:
          return JsonResponse({'msg':"no new link"})

        new_links = [peers+1]

        while(new_links[-1] < last_id):
          new_links.append(new_links[-1] + 1)
        
        request.session['peers'] = last_id

        return JsonResponse({'msg':'success','add':new_links})

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})





def play():
  pass
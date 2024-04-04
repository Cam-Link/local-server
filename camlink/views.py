from django.shortcuts import render
from camlink.models import Link

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





@csrf_exempt
def refresh(request):
  try:   

    if request.method == "GET":
      try:
        
        peers = int(request.session.get("peers",0))



        users = Link.objects.all().order_by('-id')

        


        if 0 == peers:

          length = len(users)

          if length == 0:
            return JsonResponse({'msg':"no new link"})

          new_links = []

          for i in users:
            new_links.insert(0,i.id)

          request.session['peers'] = new_links[-1]
          
          return JsonResponse({'msg':'success','add':new_links})


        last_id = int(users[0].id)

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
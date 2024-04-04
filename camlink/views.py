from django.shortcuts import render
from camlink.models import Link

import uuid

import shutil
import os
import json
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def start(request):
    if request.method == 'POST':
      
      # To Generate unique link code based on Host ID
        link_code = str(uuid.uuid1())
        
      # Set Code variable to the link code
        code = link_code
        
      # The Response data
        response_data = {
          'msg': 'success',
          'code' : link_code
        }
      
      # Cookies with 'Peers : 0'
      
        response = JsonResponse(response_data)
        response.set_cookie('Peers', '0')
      
    
    else:
        # Return an error if the request method is not POST
        return JsonResponse({'error': 'Method is not allowed.'}, status = 405)






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
from django.shortcuts import render

import os
import json
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import shutil

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








def stream(request):
   try:
      if request.method == "POST":
         try:
            chunk = request.FILES['chunk']
            num  = request.session.get("num",0)

            path = os.getcwd()+ f"/screenshare/screen/{num}.webm"
            with open (path , 'wb') as file:
               for chunk_data in chunk:
                  file.write(chunk_data)
            
            request.session['num'] = int(num)+1
            return JsonResponse({'msg':'sucess'})
         except Exception as e:
            return JsonResponse({'msg':str(e)})
      else :
         return JsonResponse({'msg':'method is not supported'}) 
          
   except:
      return JsonResponse({'msg':'Unexpected error'})






@csrf_exempt
def play(request):
  try:   

    if request.method == "GET":
      try:
        
        num = request.session.get("num",0)

        #return the requested c
        
        path = os.getcwd() + f"/screenshare/screen/{num}.webm"

        try:

          chunk = open(path, 'rb')
        except:
          return JsonResponse({'msg':"pending"})

        request.session['num'] = int(num) + 1

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
        if request.method == 'POST':
            
            # Delete the contents of the screen folder
            
            shutil.rmtree(os.getcwd() + "/screenshare/screen")
            
            return JsonResponse({'msg': 'success'})
            
        else:
            # Return an error if the request method is not POST
            return JsonResponse({'error': 'Method is not allowed.'}, status=405)
    except Exception as e:
           
            return JsonResponse({'error': str(e)}, status=500)
from django.shortcuts import render

import socket

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


host = socket.gethostbyname(socket.gethostname())
port = 8800


session = {}



def send(method,address, data={}, vid="0", blob="0"):
  global session

  url = f'https://{host}:{port}/' + address


  if method == "POST":
      if blob == "1":
          # headers = {'Content-Type':'video/webm'}
          response = requests.post(url, files=data, verify=False, cookies=session.get('session', ''))
      else:
          headers = {'Content-Type':'application/json'}
          response = requests.post(url, json=data, headers=headers, verify=False, cookies=session.get('session', ''))

  elif method == "GET":
      if blob == "1":
          headers = {'Content-Type':'video/webm'}
          response = requests.get(url, data=data, headers=headers, verify=False, cookies=session.get('session', ''))
      else:
          headers = {'Content-Type':'application/json'}
          response = requests.get(url, json=data, headers=headers, verify=False, cookies=session.get('session', ''))

  if response.cookies:
      session = response.cookies.get_dict()
  

  if vid == "1":

      content_type = response.headers.get('Content-Type')

      if 'application/json' in content_type:
          return [response.text, True]
          

      return [response.content, False]
  else:
      return response.text
































@csrf_exempt
def link(request):
  try:   

    if request.method == "POST":
      try:
          
        response = send("POST","live/link/")

        return response

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except Exception as e:
    return JsonResponse({'msg':"Unexpected error"})









@csrf_exempt
def stream(request):
  try:   

    if request.method == "POST":
      try:
          
        chunk = request.FILES

        response = send("POST","live/stream/",chunk,"0","1")

        return response

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except Exception as e:
    return JsonResponse({'msg':"Unexpected error"})








@csrf_exempt
def stop(request):
  try:   

    if request.method == "POST":
      try:
          
        response = send("POST","live/stop/")

        return response

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except Exception as e:
    return JsonResponse({'msg':"Unexpected error"})




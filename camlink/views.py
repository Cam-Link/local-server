from django.shortcuts import render
import uuid
import json
from django.http import JsonResponse
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







def link():
  pass







def stream():
  pass






def refresh():
  pass





def play():
  pass
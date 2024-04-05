from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt

def start(request):
  try:
    if request.method == 'POST':
      
        # Generate link code 
        
        link_code = "ab12" 
        
        if link_code:   
          
          response_data = {
                        'msg': 'success',
                        'code' : link_code
                    }
                   
          response = JsonResponse(response_data)
          response.set_cookie('Peers', '0')
          return response
        
        else:
              return JsonResponse({'error': 'Link code is missing.'}, status=400)
              
    else:
        # Return an error if the request method is not POST
        return JsonResponse({'error': 'Method is not allowed.'}, status=405)
      
  except Exception as e:
    return JsonResponse({'error': f'Unexpected error: {str(e)}'})







def link():
  pass







def stream():
  pass






def refresh():
  pass





def play():
  pass

from django.http import JsonResponse
from django.shortcuts import render
import google.generativeai as genai  

genai.configure(api_key="AIzaSyD-sE2PQlkrH_eIcG2ZPY8YJPpYjp-3NRg")

def generate_response(message):
    model = genai.GenerativeModel('gemini-1.5-flash')  
    response = model.generate_content(message,
                                        generation_config={
            "max_output_tokens": 200,  
            "temperature": 0.7
        }
                                      )
    return response.text.strip()

def home(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        answer = generate_response(message)
        return JsonResponse({'message': message, 'response': answer})
    return render(request, 'chatbot.html')

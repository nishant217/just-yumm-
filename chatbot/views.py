from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.conf import settings  # Import settings for API key


import google.generativeai as genai
from .models import Chat
from django.utils import timezone

# google_api_key = ''
genai.configure(api_key=settings.GOOGLE_API_KEY)


def ask_gemini(message):
    model = genai.GenerativeModel('models/gemini-1.5-pro')  
    response = model.generate_content( message)
    return response.text.strip()


def chat(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_gemini(f"Generate a recipe for {message}. Format the recipe with proper HTML formatting for better readability. Use <h3> tags for section headings, <ul> and <li> tags for ingredients, and <ol> and <li> tags for instructions. Don't use asterisks for formatting.")

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chat_app/chat2.html', {'chats': chats})

#
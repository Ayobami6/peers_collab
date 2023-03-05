from django.shortcuts import render
import openai
import os
from django.views.generic import TemplateView
from dotenv import load_dotenv
from . forms import AskForm

load_dotenv()

api_key = os.getenv("OPENAI_KEY")


def ask_gpt(request):
    data = None
    if request.method == "POST":
        openai.api_key = api_key
        user_query = request.POST.get('user_query')
        user_prompt = user_query
        chat_response = openai.Completion.create(
            model="text-davinci-003",
            prompt="You are an AI assisstant that is an Expert in Software engineering\nYou know about Software Engineering\nYou can provide advice on Linux, Programming Languages, Software Engineering Concepts and Education\n\nIf you are unable to provide an answer to a question please respond with the phrase \"I'm just an expert in Software engineering, can't help with that\n\n " + "\n" + user_prompt,
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.73,
            presence_penalty=0
        )
        data = chat_response['choices'][0]['text'].replace("?", "")
    return render(request, 'ask/ask.html', {'response': data})

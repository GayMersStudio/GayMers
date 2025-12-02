
from django.shortcuts import render


def main(request):
    context = {
        "top": "Fresh"
    }

    return render(request, "main.html", context)


def welcome(request):
    context = {}

    return render(request, "welcome.html", context)

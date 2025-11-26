
from django.shortcuts import render
from .models import Game


def default_top(request):
    context = {
        "tab": "Fresh",
        "games": [
            {
                "title": game.title,
                "desc": game.desc,
                "pic": game.pic,
                "trailer": game.trailer,
                "price": f"{str(game.price).replace('.', ',')}$" if game.price > 0 else "FREE",
            }
            for game in Game.objects.all()
        ]
    }

    if request.headers.get('HX-Request') == 'true':
        return render(request, 'tabs/fresh.html', context)

    return render(request, "main.html", context)


def welcome(request):
    context = {
        
    }

    return render(request, "welcome.html", context)


def sign_up(request):
    context = {
        
    }

    return render(request, "sign_up.html", context)


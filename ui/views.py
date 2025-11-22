from django.shortcuts import render


def default_top(request):
    context = {
        "tab": "Fresh",
        "games": [{
            "pic": "https://clan.fastly.steamstatic.com/images//3703047/98be0d0a60eca8edbad91ec0050918f83ea462e2.png",
            "title": "Dota 2",
            "desc": """The most-played game on Steam.
Every day, millions of players worldwide enter battle as one of over a hundred Dota heroes. And no matter if it's their 10th hour of play or 1,000th, there's always something new to discover. With regular updates that ensure a constant evolution of gameplay, features, and heroes, Dota 2 has truly taken on a life of its own.
"""
        }]*10
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




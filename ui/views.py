from django.shortcuts import render


def default_top(request):
    context = {
        "tab": "default_top",
        "games": [{
            "pic": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/570/capsule_231x87.jpg?t=1762820658"
        }]*2
    }

    if request.headers.get('HX-Request') == 'true':
        return render(request, 'tabs/default_top.html', context)

    return render(request, "main.html", context)

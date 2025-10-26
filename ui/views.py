from django.shortcuts import render


def default_top(request):
    context = {
        "tab": "default_top"
    }

    if request.headers.get('HX-Request') == 'true':
        return render(request, 'tabs/default_top.html', context)

    return render(request, "main.html", context)

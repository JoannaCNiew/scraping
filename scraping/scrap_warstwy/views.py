from django.shortcuts import render

def warstwy(request):
    return render(
        request,
        'scrap_warstwy/warstwy.html'
    )
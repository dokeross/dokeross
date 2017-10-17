from django.shortcuts import render

def doker_page(request):
    return render(request, 'doker_page/doker.html', {})
from django.shortcuts import render

def office_page(request):
    return render(request, 'office_page/office.html', {})
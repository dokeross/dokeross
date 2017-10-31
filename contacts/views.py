from django.shortcuts import render

def contacts_page(request):
    return render(request, 'contacts_page/contacts.html', {})
from django.shortcuts import render

def contact_page(request):
    """
    Renders the contact us page.
    """
    return render(request, 'contact.html')

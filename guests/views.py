from django.shortcuts import render


def DisplayContact(request):
    """
    Displays the Contact page
    """
    return render(request, 'contact.html')


def DisplayHome(request):
    """
    Displays the Homepage
    """
    return render(request, 'home.html')

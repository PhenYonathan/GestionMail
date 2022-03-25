from django.shortcuts import render

# Create your views here.


def manage_mail(request):
    return render(request, "manage_mail/index.html")

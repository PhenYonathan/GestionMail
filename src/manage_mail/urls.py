from django.urls import path

from manage_mail.views import manage_mail

urlpatterns = [
    path('manage/', manage_mail),
]

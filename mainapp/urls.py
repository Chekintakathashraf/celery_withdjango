from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('', views.test, name="test"),
    path('sendmailtoall', views.send_mail_to_all, name="test"),
    path('schedulemail', views.schedule_mail, name="test"),
]
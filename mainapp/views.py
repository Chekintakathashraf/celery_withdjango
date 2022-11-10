from django.shortcuts import render,HttpResponse
from .task import test_func
from send_email_app.task import send_mail_func

from django_celery_beat.models import PeriodicTask,CrontabSchedule
# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay() 
    return HttpResponse("Sent")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 0, minute = 17)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"1",task=' send_email_app.taşk.send_mail_func')
    return HttpResponse("Done")

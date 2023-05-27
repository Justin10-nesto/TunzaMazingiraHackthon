from django.shortcuts import render, redirect
from .models import ScheduleTask, Place
# Create your views here.
def addSchedule(request):
    if request.method == 'POST':
        Date = request.POST.get('Date')
        description = request.POST.get('description')
        id = request.POST.get('name')
        name = Place.objects.filter(id = id).first()
        ScheduleTask.objects.create(place = name, date_used = Date, message = description)
        return redirect('viewSchedule')
    place = Place.objects.all()
    context = {'place':place}
    return render(request, 'add-schedule.html', context)

def viewSchedule(request):
    schedules = ScheduleTask.objects.all()
    context = {'schedules':schedules}
    return render(request, 'list-schedule.html', context)


def deleteSchedule(request, id):
    schedules = ScheduleTask.objects.filter(id = id)
    schedules.delete()
    return redirect('viewSchedule')

def sending_mesage(request):
    schedules = ScheduleTask.objects.all()
    username = ''
    api_key = ''
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    response = sms.send(sms, [number])


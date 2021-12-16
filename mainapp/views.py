from django.shortcuts import render
from .models import Contract
from rest_framework.decorators import api_view
from django.http import JsonResponse
import datetime

def container_redirect(list):
    for element in list:
        #execute bash script with element...port as $1
        print(element)

#bash
#just change port in container to redirect to expired page
# port+django page
@api_view(['GET','POST',])
def api_reminder(request):
    contracts = Contract.objects.all()
    this_day = datetime.date.today()
    list = []
    for c in contracts:
        if (this_day>c.end_date):
            c.is_active=False
            c.save()
            list.append(c.name)
    container_redirect(list)
    response_content={'Result':'Done'}
    return JsonResponse(response_content,safe=False)

def show_expired(request):
    return render(request,'expired.html')

def show_container_done(request):
    return render(request,'container-done.html')

#from django.template.loader import get_template
#from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    now = datetime.datetime.now()
    #t = get_template('hello.html')
    #html = t.render({'current_date': now})
    #return HttpResponse(html)
    return render(request, 'hello.html', {'current_date': now})

def root_view(request):
    return HttpResponse("Hello root");

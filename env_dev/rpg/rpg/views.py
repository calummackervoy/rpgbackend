#from django.template.loader import get_template
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from rpg.forms import CharacterForm

def hello(request):
    now = datetime.datetime.now()
    #t = get_template('hello.html')
    #html = t.render({'current_date': now})
    #return HttpResponse(html)
    return render(request, 'hello.html', {'current_date': now})

def root_view(request):
    # request.META['HTTP_USER_AGENT', 'unknown']  # HTTP headers of req
    return HttpResponse("Hello root");

def new_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #TODO: submit to database
            return HttpResponse("success");
    else:
        form = CharacterForm()

    return render(request, 'create/form_new_character.html', {'form': form})

def display_meta(request):
    values = request.META
    html = []
    for k in sorted(values):
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

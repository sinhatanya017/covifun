from django.shortcuts import render

from .models import My_work

# Create your views here.


def index(request):
    work = My_work.objects.all()
    return render(request, 'index.html', {'work': work})

def about(request):
    work = My_work.objects.all()
    return render(request, 'about.html', {'work': work})

def contact(request):
    #work = My_work.objects.all()
    return render(request, 'contact.html')

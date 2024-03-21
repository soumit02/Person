from django.shortcuts import render
from persons.models import Person

def home(request):
    persons=Person.objects.all()
    return render(request,'home.html',{
        "persons":persons,
    })
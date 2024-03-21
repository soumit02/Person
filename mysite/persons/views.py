from django.http import HttpResponse
from django.shortcuts import render
from .import forms
from .models import Person
# Create your views here.
def add_person(request):
    if request.method == "GET":
        form=forms.PersonForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse("add successful")
    else:
        form = forms.PersonForm()
    return render(request,'forms.html',{
        "form":form,
    })

def update_person(request,p_id):
   p = Person.objects.get(pk=p_id)
   if request.method == "GET":
       form = forms.PersonForm(request.GET or None ,instance=p)
       if form.is_valid():
           form.save()
           return HttpResponse("update successful")
   else:
       form = forms.PersonForm(instance=p)
   return render(request, 'forms.html', {
       "form": form,
   })

def delete_person(request,p_id):
    Person.objects.get(pk=p_id).delete()
    return HttpResponse("delete successfully")


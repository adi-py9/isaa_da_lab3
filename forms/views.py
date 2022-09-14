from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
def AddNewcontact(request):
    form=ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home")
    context={'forms':form}
    return render(request,'contact.html',context)
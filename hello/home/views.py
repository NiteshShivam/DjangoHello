from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context = {
        'variable':'this is a sent'
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
    return HttpResponse("This is about page")
def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name,phone=phone,email=email,desc=desc,data = datetime.today())
        contact.save()
        messages.success(request, "Information saved")

    return render(request,'contact.html')
    return HttpResponse("Don't contact")
def services(request):
    return render(request,'services.html')
    return HttpResponse("Don't services")
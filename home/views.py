from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    # context ={
    #     'variable' : "this is sent"
    # }
    # return render(request, 'contact.html', context)    # for declaring variable
    return render(request,'index.html')
    # return HttpResponse("This is Home page")
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name ,email =email , phone = phone , desc =desc , date = datetime.today())
        messages.success(request, 'Your Message has been sent.')
        contact.save()

    return render(request, 'contact.html')
    # return HttpResponse("7988282452 ")

from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
import requests
# Create your views here.
def index(request):
    url = "https://cinemos.p.rapidapi.com/news/bollywood"
    headers = {
        "X-RapidAPI-Key": "bb261d1944mshbecf2191efa410ep12b54cjsne765765377bf",
        "X-RapidAPI-Host": "cinemos.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    response=response.json()
    return render(request, 'index.html',{'res':response})
    # # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 
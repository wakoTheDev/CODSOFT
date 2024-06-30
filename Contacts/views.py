from django.shortcuts import render,redirect
from django.contrib import messages
from django.template import loader
from .models import ContactRecord

# Create your views here.
def home(request):
    numbers  = ContactRecord.objects.all()
    return render(request,'home.html',{'numbers':numbers})

def create(request):
    if request.method == 'post':
        first_name = request.POST.get('first')
        last_name = request.POST.get('last')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone-no')
        address = request.POST.get('address')
        if first_name and last_name:
            if email and address:
                if phone_number:
                    if ContactRecord.objects.filter(phone_number=phone_number).exists():
                        messages.info(request,'phone number already exist')
                        return redirect('create')
                    else:
                        contact = ContactRecord.objects.create(first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                address=address,
                                                phone_number=phone_number)
                         
                        contact.save()
                        messages.info(request,'saved sucessfully')
                        return redirect('home')
                else:
                    messages.info(request,'phone number is missing')
                    return redirect('create')
            else:
                messages.info(request,'email or address missing') 
                return redirect('create')     
        else:
            messages.info(request,'first name  or last name missing') 
            return redirect('create')
    else:
        return render(request,'create.html')


def search(request):    
    if request.method =='POST':
        search = request.POST.get('Search-bar')
        is_available = ContactRecord.objects.filter(first_name=search) 
        if is_available:       
            return render(request,'retrieve.html',{'is_available':is_available}) 
        else:
            messages.info(request,'Contact not found')
            return redirect('search')
    else:
        return render(request,'retrieve.html')


def removed(request,id):
    if request.method == 'POST':
        input_code = int(input())
        if input_code == 1 :
            warning = False
        else:
            warning = True
            ContactRecord.objects.delete(first_name.id==id)
            messages.info(request,'contact record deleted successfully')
            warning = False
            return redirect('home')
            

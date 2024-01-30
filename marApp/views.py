from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    allItem = Item.objects.all()
    context={"all":allItem}
    return render(request, 'home.html', context)

def about(request):
    allStaff = Staff.objects.all()
    context={"all":allStaff}
    return render(request, 'about.html', context)

def contact(request):
    if request.method=="POST":
        #marrja e informacioneve nga input
        name = request.POST['name_contact']
        surname = request.POST['surname_contact']
        email = request.POST['email_contact']
        comment = request.POST['comment_contact']
        #kalimi ne databaze
        Contact(
            contact_name = name,
            contact_surname = surname,
            contact_position = comment,
            contact_email = email
            
        ).save()
    return render(request, 'contact.html')

def detail(request, id):
    detailItem = Item.objects.get(pk=id)
    context = {"detail": detailItem}
    return render(request, 'detail.html', context)
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    allItem = Item.objects.all()
    context={"all":allItem}
    return render(request, 'home.html', context)

# def about(request):
    allStaff = Staff.objects.all()
    context={"all":allStaff}
    return render(request, 'about.html', context)

def reservation(request):
    if request.method=="POST":
        #marrja e informacioneve nga input
        name = request.POST['name_reservation']
        email = request.POST['email_reservation']
        time = request.POST['time_reservation']
        date = request.POST['date_reservation']
        people = request.POST['people_reservation']
        phone = request.POST['phone_reservation']
        #kalimi ne databaze
        Reservation(
            reservation_name = name,
            reservation_time = time,
            reservation_date = date,
            reservation_email = email,
            reservation_people = people,
            reservation_phone = phone
            
        ).save()
    return render(request, 'reservation.html')



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
    return render(request, 'menu.html')

def detail(request, id):
    detailItem = Item.objects.get(pk=id)
    context = {"detail": detailItem}
    return render(request, 'detail.html', context)
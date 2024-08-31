from django.db import models

#tabelat e databazes aka modele ose klasa


class Item(models.Model):
    item_name = models.CharField(max_length=30, null=True, blank=True)
    item_text = models.TextField(max_length=30, null=True, blank=True)
    item_image = models.ImageField(upload_to='item/')
    
    def __str__(self):
        return f"{self.item_name}"




class Staff(models.Model):
    staff_name = models.CharField(max_length=15, null=True, blank=True)
    staff_surname = models.CharField(max_length=15, null=True, blank=True)
    staff_position = models.CharField(max_length=20, null=True, blank=True)
    staff_email = models.EmailField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.staff_name} {self.staff_surname}/ {self.staff_position}"
    


class Reservation(models.Model):
    reservation_name = models.CharField(max_length=15, null=True, blank=True)
    reservation_email = models.EmailField(max_length=30, null=True, blank=True)
    reservation_time = models.TimeField(max_length=20, null=True, blank=True)
    reservation_date = models.DateField(max_length=20, null=True, blank=True)
    reservation_people = models.CharField(max_length=3, null=True, blank=True)
    reservation_phone = models.CharField(max_length=20, null=True, blank=True)

def __str__(self):
        return f"{self.reservation_name} {self.reservation_email}"
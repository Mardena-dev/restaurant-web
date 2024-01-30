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
    


class Contact(models.Model):
    contact_name = models.CharField(max_length=15, null=True, blank=True)
    contact_surname = models.CharField(max_length=15, null=True, blank=True)
    contact_position = models.CharField(max_length=20, null=True, blank=True)
    contact_email = models.EmailField(max_length=30, null=True, blank=True)

def __str__(self):
        return f"{self.contact_name} {self.contact_surname}"
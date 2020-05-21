from django.db import models
from datetime import  datetime
# Create your models here.

ETAT_CHOICES = (

    ('N', 'nouveau'),
    ('R', 'rupture'),
    ('P', 'promotion')
)

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('C', 'chaussures'),
    ('A', 'accessoires')
)

class Produit(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    price = models.IntegerField()
    slug = models.SlugField(max_length=48)
    etat = models.CharField(choices=ETAT_CHOICES, max_length=1, default='N', blank=True)
    active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Wilaya(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Commune(models.Model):
    Wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Checkout(models.Model):
    produit = models.ForeignKey('Produit', on_delete=models.CASCADE)
    prix = models.IntegerField(default=0)
    nom_du_client = models.CharField(max_length=40)
    prenom_du_client = models.CharField(max_length=40)
    adresse_du_client = models.CharField(max_length=40)
    date_added = models.DateTimeField(auto_now_add=True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.SET_NULL, null=True, blank=True)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    confirmer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.produit)

    def get_prix(self):
        return self.prix * self.quantity
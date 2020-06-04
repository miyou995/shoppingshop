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


COUT_LIVRAISON = (
    (400, 'alger'),
    (600, 'autres'),
)

class Produit(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    image = models.ImageField(upload_to='media/produits',blank = True)
    etat = models.CharField(choices=ETAT_CHOICES, max_length=1, default='N', blank=False)
    active = models.BooleanField(default=True)

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

class Order(models.Model):
    produit = models.ForeignKey('Produit', on_delete=models.CASCADE)
    prix = models.IntegerField(default=0)
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    telephone = models.CharField(max_length=20, default='', blank=True)
    email = models.EmailField(blank=True)
    adresse = models.CharField(max_length=40)
    # livraison = models.IntegerField(choices=COUT_LIVRAISON,  default=600, blank=False)
    livraison = models.IntegerField(default=600, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.SET_NULL, null=True, blank=True)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    confirmer = models.BooleanField(default=False)
    total = models.IntegerField(default=0)



    def __str__(self):
        return str(self.produit)

    # def get_price(self):
    #     return self.prix * self.quantity
        # print('prix: ', self.prix)
        # print('quanitté: ', self.quantity)
        # print('cout de livraison: ', self.cout_livraison)
    

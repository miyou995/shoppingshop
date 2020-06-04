
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ModelFormMixin, CreateView
from django.urls import reverse

from .models import Produit, Order, Wilaya, Commune
from .forms import OrderCreateForm
from django.http import HttpResponse

from  django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404


@staff_member_required
def admin_order_detail(request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'admin/main/order/detail.html', {'order': order}) 




class ProductListView(ListView):
    template_name = 'index.html'
    model = Produit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produit"] = Produit.objects.all()
        return context

class ProductDetailView(CreateView, DetailView):
    model = Produit
    form_class = OrderCreateForm
    context_object_name = 'produit'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["form"] = self.get_form()
        context["wilayas"]= Wilaya.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        # self.object = self.get_object()
        # form = self.get_form()
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.produit = self.get_object()
            order.prix = self.get_object().price

            

            
            wilaya = str(form.cleaned_data['wilaya'])
            commune = str(form.cleaned_data['commune'])

            quantity = form.cleaned_data['quantity']
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            adresse = form.cleaned_data['adresse']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']

            if wilaya == 'Alger':
                livraison = 400
            else:
                livraison = 600

            order.livraison = livraison 

            total_price = order.quantity * order.prix
            total_facture = total_price + livraison
            order.total = total_facture

            

            print(wilaya, commune)
         
            order.save()
            form = OrderCreateForm()
            return redirect(f'/{self.get_object().pk}')
        
        print(form.errors)
        return redirect(f'/{self.get_object().pk}')
        

def load_communes(request):
    wilaya_id = request.GET.get('wilaya')
    communes = Commune.objects.filter(Wilaya__id=wilaya_id)
    return render(request, 'main/commune_dropdown_list_options.html', {'communes': communes})


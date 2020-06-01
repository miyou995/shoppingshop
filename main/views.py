from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ModelFormMixin, CreateView
from django.urls import reverse

from .models import Produit, Order, Wilaya, Commune
from .forms import OrderCreateForm
from django.http import HttpResponseRedirect

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
            order.price = self.get_object().price
            

            wilaya = str(form.cleaned_data['wilaya'])
            commune = str(form.cleaned_data['commune'])

            quantity = form.cleaned_data['quantity']
            nom_du_client = form.cleaned_data['nom_du_client']
            prenom_du_client = form.cleaned_data['prenom_du_client']
            adresse_du_client = form.cleaned_data['adresse_du_client']
            livraison = order.cout_livraison

            if wilaya == 'Alger':
                livraison = 400
            else:
                livraison = 600


            total_price = order.quantity * order.price
            total_facture = total_price + livraison
            order.montant_total = total_facture

            

            print(wilaya, commune)
         
            order.save()
            form = OrderCreateForm()
            return redirect(f'/{self.get_object().pk}')
            print('jusque la cv')
        
        print(form.errors)
        return redirect(f'/{self.get_object().pk}')
        

def load_communes(request):
    wilaya_id = request.GET.get('wilaya')
    communes = Commune.objects.filter(Wilaya__id=wilaya_id)
    return render(request, 'main/commune_dropdown_list_options.html', {'communes': communes})


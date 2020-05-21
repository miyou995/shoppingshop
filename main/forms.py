from django import forms 
from .models import Checkout, Commune , Wilaya
class CheckoutCreateForm(forms.ModelForm):
    class Meta:
        model = Checkout 
        fields = ['nom_du_client', 'prenom_du_client','adresse_du_client', 'quantity']

    # def __init__(self, *args, **kwargs):
    #     super(CheckoutCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['wilaya']=forms.ModelChoiceField(queryset=Wilaya.objects.all())
    #     self.fields['commune']=forms.ModelChoiceField(queryset=Commune.objects.all())


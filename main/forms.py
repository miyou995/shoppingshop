from django import forms 
from .models import Order, Commune , Wilaya
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ['nom', 'prenom', 'adresse', 'quantity', 'wilaya', 'commune', 'email', 'telephone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['wilaya'] = forms.ModelChoiceField(queryset=Wilaya.objects.all()) 
        # self.fields['commune'] = forms.ModelChoiceField(queryset=Commune.objects.all()) 
        self.fields['commune'].queryset = Commune.objects.none()

        if 'wilaya' in self.data:
            try:
                wilaya_id = int(self.data.get('wilaya'))
                self.fields['commune'].queryset = Commune.objects.filter(Wilaya_id=wilaya_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif not 'wilaya' in self.data:
            self.fields['commune'].queryset = Commune.objects.none()
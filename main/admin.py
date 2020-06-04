from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse 
from django.utils.safestring import mark_safe
from .models import Produit, Order, Wilaya, Commune

from import_export import resources
from import_export.admin import ExportMixin
from import_export.fields import Field
import csv
import datetime


# def export_to_csv(modeladmin, request, queryset):
#     opts = modeladmin.model._meta
#     content_disposition = f'attachment; filename= {opts.verbose_name}.csv'
#     response = HttpResponse(content_type='text/csv')
#     response['Conetent-Disposition'] = content_disposition
#     writer = csv.writer(response)

#     fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
#     writer.writerow([field.verbose_name for field in fields])

#     for obj in queryset:
#         data_row = []
#         for field in fields:
#             value = getattr(obj, field.name)
#             if isinstance(value, datetime.datetime):
#                 value = value.strftime('%d/%m/%Y')
#             data_row.append(value)
#         writer.writerow(data_row)
#     return response
# export_to_csv.short_descrition = 'Export to csv'

# def order_detail(obj):
#         url = reverse('main:admin_order_detail', args=[obj.id])
#         return mark_safe(f'<a href="{url}">View</a>') 

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'active')
    list_display_links = ('id', 'name')
    list_display_links = ('id','name',)
    list_per_page = 40
    list_editable = ['active']
    list_filter = ('name',)
    readonly_fields = ('date_added',)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('id', 'name',)


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id','produit', 'nom', 'date_added')
#     list_display_links =('id','produit')
#     search_fields = ('id',)
#     list_per_page = 25
#     readonly_fields = ('date_added',)
    # actions = [export_to_csv]


class OrderResource(resources.ModelResource):
    signature = Field(column_name='signature')

    class Meta:
        model = Order
        exclude = ('confirmer', )
        fields = ('id', 'produit__name', 'prix', 'total', 'wilaya__name', 'commune__name', 'quantity', 'prenom', 'nom')
        export_order = ('id', 'produit__name', 'prix', 'quantity', 'total', 'prenom', 'nom', 'wilaya__name', 'commune__name')


@admin.register(Order)
class ViewAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'produit', 'nom', 'prix', 'date_added', 'wilaya', 'commune', 'total')
    list_display_links =('id','produit')
    search_fields = ('id', 'produit__name', 'nom', 'prenom', 'wilaya__name', 'commune__name')
    list_filter = ('date_added', 'wilaya')
    list_per_page = 25
    readonly_fields = ('date_added',)
    resource_class = OrderResource

class WilayaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions






admin.site.register(Produit, ProduitAdmin)
admin.site.register(Wilaya, WilayaAdmin)
admin.site.register(Commune)



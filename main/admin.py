from django.contrib import admin
from .models import Produit, Checkout, Wilaya, Commune

from import_export.admin import ImportExportModelAdmin
import csv
import datetime
from django.http import HttpResponse

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



class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'active', 'in_stock')
    list_display_links = ('id', 'name')
    list_display_links = ('id','name')
    list_per_page = 40
    list_editable = ['active', 'in_stock']
    list_filter = ('name', 'in_stock')
    readonly_fields = ('date_added',)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('id', 'name',)


# class CheckoutAdmin(admin.ModelAdmin):
#     list_display = ('id','produit', 'nom_du_client', 'date_added')
#     list_display_links =('id','produit')
#     search_fields = ('id',)
#     list_per_page = 25
#     readonly_fields = ('date_added',)
    # actions = [export_to_csv]

@admin.register(Checkout)
class ViewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','produit', 'nom_du_client', 'date_added')
    list_display_links =('id','produit')
    search_fields = ('id',)
    list_per_page = 25
    readonly_fields = ('date_added',)


admin.site.register(Produit, ProduitAdmin)
admin.site.register(Wilaya)
admin.site.register(Commune)


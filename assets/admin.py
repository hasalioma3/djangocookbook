from django.contrib import admin
from .models import Categories, Assets
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import forms
from django.urls import path
# import HttpResponseRedirect from django

from django.contrib import messages
from django.shortcuts import render, redirect
import datetime
import csv
from django.utils.encoding import smart_str

admin.site.site_header = "Naivas Assets Admin"
admin.site.site_title = "Naivas Admin Portal"
admin.site.index_title = "Welcome to Naivas Assets Portal"

# Register your models here.
# export csv of the data
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([smart_str(getattr(obj, field)) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

# import asset csv
class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class CategoriesAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('name',)
    search_fields = ('name',)
    actions = [ "export_as_csv"]
class AssetsAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('name', 'description', 'category', 'price', 'serial_No', 'barcode', 'created', 'updated')
    search_fields = ('name', 'description', 'category__name', 'serial_No', 'barcode', 'created', 'updated')
    list_filter = ('category',)
    actions = [ "export_as_csv"]
    change_list_template = "assets/change_list.html"
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file')
                return HttpResponseRedirect(request.path_info)
            data_set = csv_file.read().decode('UTF-8')
            csv_data = data_set.split("\n")
            # count rows in a csv
            row_count = len(csv_data)
           
            try:
                for row in csv_data:
                    fields = row.split(",")
                    created = Assets.objects.get_or_create( 
                        name=fields[0],  
                        description = fields[1],
                        category=Categories(id=fields[2]),
                        price=fields[3], 
                        serial_No=fields[4],
                        barcode=fields[5],
                        created=datetime.datetime.now(), 
                        updated=datetime.datetime.now()
                    )
                    
                    # check if error
                if created[1] == True:
                    messages.success(request, "Sucessfully created " + str(row_count) + " assets")
                else:
                    messages.error(request, "Not Created")
            except Exception as e:
                messages.error(request, e)
            # return HttpResponse("The following Error Occured : " + str(e))
            # return HttpResponseRedirect("../")
            return redirect('admin:assets_assets_changelist')
        form = CsvImportForm()
        payload = {'form': form}
        return render(request, 'assets/import.html', payload)



admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Assets, AssetsAdmin)



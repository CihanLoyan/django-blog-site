from django.contrib import admin
from .models import yazi


class adminYazi(admin.ModelAdmin):
    list_display = ['baslik', "yayinTarihi", "slug"]
    list_display_links = ["baslik", "yayinTarihi"]
    list_filter = ["yayinTarihi"]
    search_fields = ["baslik"]
    # list_editable = [""]  nesnenin içine girmeden içerik değişikliği yapılmasını sağlar. 

    class Meta:
        model = yazi
         
admin.site.register(yazi, adminYazi)

# Register your models here.

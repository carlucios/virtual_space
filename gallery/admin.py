from django.contrib import admin

from gallery.models import Fotografia

class List_Fotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "legenda", "publicar")
    list_display_links = ("id", "nome", "legenda")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicar",)
    list_per_page = 50

admin.site.register(Fotografia, List_Fotografias)

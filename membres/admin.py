from django.contrib import admin
from . models import membres

# Register your models here.
class MembresAdmin(admin.ModelAdmin):
    list_display = "nom","email","mot_de_passe","adresse","telephone"

admin.site.register(membres,MembresAdmin)

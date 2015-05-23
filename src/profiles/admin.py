from django.contrib import admin

# Register your models here.
#Para adicionar el modelo a la interfaz de administrador
from .models import profile

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile, profileAdmin)
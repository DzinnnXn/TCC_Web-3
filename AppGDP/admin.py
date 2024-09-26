from django.contrib import admin

# Register your models here.
from .models import Senai
from .models import Inventario

admin.site.register(Senai)
admin.site.register(Inventario)
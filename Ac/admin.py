from django.contrib import admin

# Register your models here.
from .models import extendeduser, Quize

admin.site.register(extendeduser)
admin.site.register(Quize)
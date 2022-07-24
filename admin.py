from django.contrib import admin
from . models import About,Card,Rasm,Karta,Picture

# Register your models here.

admin.site.register(About),
admin.site.register(Card),
admin.site.register(Rasm),
admin.site.register(Karta),
admin.site.register(Picture)


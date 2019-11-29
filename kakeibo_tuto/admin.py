from django.contrib import admin

# Register your models here.
from .models import Category, Suitoh,Ranks


class SuitohAd(admin.ModelAdmin):
   list_display=('data','cat','meimoku','out_cost','rank')


admin.site.register(Category)
admin.site.register(Suitoh,SuitohAd)
admin.site.register(Ranks)
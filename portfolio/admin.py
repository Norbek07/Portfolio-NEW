from django.shortcuts import render
from django.contrib import admin
from .models import Contact,PortfolioItem,Blog,Comment,Category,Gallery,Books,About
from django.utils.html import format_html
# Register your models here.


admin.site.register((Comment,Category,Blog,Books))


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    readonly_fields = ['id']
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  
  
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('img','title','description')
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('img', 'title', 'created_date')
    readonly_fields = ['id']

    def img(self, obj):
        return format_html(
            '<img width="100" height="100" src="{}" style="border-radius: 50%;" />',
            obj.image.url
        )
    

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('img','title' ,'description', 'created_date')
    readonly_fields = ['id']
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}" style="border-radius: 50%;"/>'.format(obj.image.url))
  
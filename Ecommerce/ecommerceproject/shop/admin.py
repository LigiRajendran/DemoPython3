from django.contrib import admin


from .models import Category, Product

class CategoryAdmin (admin.ModelAdmin):
     list_display=['name','slug']
     prepopulated_fields = {'slug':('name',)}

     class Meta:
          model = Category
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
     list_display=['name','slug', 'price','stock', 'availbale','created','updated']
     list_editable = ['price','stock', 'availbale']
     prepopulated_fields = {'slug':('name',)}
     list_per_page = 20
     class Meta:
          model = Product
admin.site.register(Product,ProductAdmin)

# Register your models here.

from django.contrib import admin
from .models import Category,Laptop,Book,Shoe,Author,Brand,Publisher,Producer,User,CartItem,Cart,Product
# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Laptop)
admin.site.register(Category)
admin.site.register(Shoe)
admin.site.register(Brand)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Producer)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Product)
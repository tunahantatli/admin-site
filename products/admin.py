from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)

admin.site.site_title = "tunahantatli.co"
admin.site.site_header = "Admin Portal"
admin.site.index_title = "Welcome to tunahantatli.co Admin Portal"

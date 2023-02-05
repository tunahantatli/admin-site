from django.contrib import admin
from .models import Product
from django.utils import timezone

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date","added_days_ago",)
    list_editable = ( "is_in_stock", )
    # list_display_links = ("create_date", ) #can't add items in list_editable to here
    list_filter = ("is_in_stock", "create_date")
    ordering = ("-update_date",)  
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)}   # when adding product in admin site
    list_per_page = 25
    date_hierarchy = "update_date"
    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description",),
            'description' : "You can use this section for optionals settings"
        })
    )
    actions = ("is_in_stock", )

    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} kinds of products added to stock.")
        
    is_in_stock.short_description = 'Add Selected Products to Stock'
    
    # def added_days_ago(self, product):
    #     fark = timezone.now() - product.create_date
    #     return fark.days


admin.site.register(Product, ProductAdmin)

admin.site.site_title = "tunahantatli.co"
admin.site.site_header = "Admin Portal"
admin.site.index_title = "Welcome to tunahantatli.co Admin Portal"

from django.contrib import admin
from employee.models import Employee, EmployeeType, Product
# Register your models here.


# Admin Action Functions
def change_gender(modeladmin, request, queryset):
    queryset.update(gender='Male')

# Action description
change_gender.short_description = "Mark Selected Gender as Male"


class EmployeeAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    date_hierarchy = 'created_at'
    search_fields = ['name', 'address', 'gender']
    list_display = ('name', 'address','email','gender','age','mobile','type','get_products')
    list_display_links = ('name', 'address')
    list_select_related = ('type',)
    list_filter = ('name',)
    # prepopulated_fields ={'product': ('product',)}
    # raw_id_fields =("product",)
    actions = [change_gender]

    def get_products(self, obj):
        return ", ".join([p.name for p in obj.product.all()])


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(EmployeeType)
admin.site.register(Product)

admin.site.site_header = "Sanket Sawardekar"
admin.site.site_title = "Ecommerce"
admin.site.index_title = ''
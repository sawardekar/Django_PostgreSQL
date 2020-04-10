from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from employee.models import Employee, EmployeeType, Product
# Register your models here.


# Admin Action Functions
def change_gender(modeladmin, request, queryset):
    queryset.update(gender='Male')


# Action description
change_gender.short_description = "Mark Selected Gender update as Male"


class EmployeeAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    # fields = ('name', 'address', 'gender','age')
    # readonly_fields = ('age',)
    sortable_by = 'id'
    date_hierarchy = 'created_at'
    search_fields = ['name', 'address', 'gender']
    list_display = ('image_tag', 'name', 'address','email','gender','age','mobile','type','get_products','display_age')
    list_display_links = ('name', 'address')
    list_select_related = ('type',)
    list_filter = ('name',)
    list_editable = ('age',)
    actions = [change_gender]
    # fieldsets = [
    #     ('Body', {'classes': ('full-width',), 'fields': ('address',)})
    # ]
    change_list_template = 'admin/admin_filter_list.html'

    def get_products(self, obj):
        return ", ".join([p.name for p in obj.product.all()])

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('age/<int:age_count>/', self.update_age)
        ]
        return custom_urls + urls

    def update_age(self, request, age_count):
        self.model.objects.all().update(age=age_count)
        self.message_user(request, 'All Employee Age changes Successfully')
        return HttpResponseRedirect("../")

    def display_age(self, obj):
        display_size = obj.age if obj.age <= 60 else 60
        return format_html(
            f'<span style="font-size : {display_size}px;">{obj.age}</span>'
        )


admin.site.unregister(Group)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeType)
admin.site.register(Product)

admin.site.site_header = "Admin DashBoard"
admin.site.site_title = "Ecommerce"
admin.site.index_title = ''


# install django suit using below command
# pip install https://github.com/darklow/django-suit/tarball/v2
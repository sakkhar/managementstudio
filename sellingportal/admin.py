from django.contrib import admin

# Register your models here.
from sellingportal.models import Student, Degree


class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'age', 'date_birth']
    list_display = ('first_name', 'last_name', 'age', 'date_birth')
    search_fields = ('first_name', 'last_name', 'age', 'date_birth')

admin.site.register(Student, StudentAdmin)
admin.site.register(Degree)
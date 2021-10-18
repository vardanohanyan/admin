from django.contrib import admin
from .models import Person
# admin.site.register(Person)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name',)

    def upper_case_name(self, obj):
        return(obj.name + ' ' + obj.shirt_size).upper()

    upper_case_name.short_description = 'Name'
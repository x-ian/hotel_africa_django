from django.contrib import admin

from .models import Facility
from .models import FacilityPhoto
from .models import Unit
from .models import UnitPhoto
from .models import *
from django.db import models

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import SafeData, SafeString, mark_safe

class PhotoWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f' <a href="{image_url}" target="_blank">'
                f'  <img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(PhotoWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))

class UnitBedAdmin(admin.TabularInline):
    model = UnitBed
    extra = 1
    classes = ['collapse']

class UnitPhotoAdmin(admin.TabularInline):
    model = UnitPhoto
    extra = 1
    formfield_overrides = {
        models.ImageField: {'widget': PhotoWidget}
    }
    classes = ['collapse']

class UnitAdmin(admin.ModelAdmin):
    model = Unit
    inlines = [ UnitPhotoAdmin, UnitBedAdmin]
    fieldsets = (
        (None, {
            'fields': ('name', 'facility', 'quantity_of_units_in_facility', 'kind', 'max_people', 'square_meters')
        }),
        ('Internet', {
            'classes': ('collapse',),
            'fields': ('internet_access', 'internet_free_of_charge')
        }),
        ('Furnishing', {
            'classes': ('collapse',),
            'fields': ('furnishing_sitting_area', 'furnishing_sofa', 'furnishing_desk', 'furnishing_extras')
        }),
        ('Amenities', {
            'classes': ('collapse',),
            'fields': ('amenity_ac', 'amenity_fan', 'amenity_tv', 'amenity_private_bathroom', 'amenity_shower', 'amenity_towels', 'amenity_mosquito_net', 'amenity_private_entry', 'amenity_smoking', 'amenity_pets', 'amenity_wheelchair', 'amenity_extras')
        }),
        ('Misc', {
            'classes': ('collapse',),
            'fields': ('views',)
        })
    )

class FacilityLanguageAdmin(admin.TabularInline):
    model = FacilityLanguage
    extra = 1
    classes = ['collapse']

class FacilityPhotoAdmin(admin.TabularInline):
    model = FacilityPhoto
    extra = 1
    formfield_overrides = {
        models.ImageField: {'widget': PhotoWidget}
    }
    classes = ['collapse']

class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    inlines = [ FacilityPhotoAdmin, FacilityLanguageAdmin]
    fieldsets = (
        (None, {
            'fields': ('name','arrival', 'contact_email', 'contact_phone_1', 'contact_phone_2', 'policies', 'directions',)
        }),
        ('Address & Location', {
            'classes': ('collapse',),
            'fields': ('address_street_1', 'address_street_2', 'address_city', 'address_zip', 'address_state', 'address_country', 'location_lat', 'location_long'),
        }),
        ('Specialities', {
            'classes': ('collapse',),
            'fields': ('speciality_beach', 'speciality_swimming_pool', 'speciality_fitness_room', 'speciality_bar', 'speciality_restaurant_meal_breakfast', 'speciality_restaurant_meal_dinner', 'speciality_restaurant_meal_lunch', 'speciality_restaurant_prices', 'speciality_restaurant_times', 'speciality_kids_playground', 'speciality_airport_shuttle', 'speciality_24h_front_desk', 'speciality_extras'),
        }),
        ('Misc', {
            'classes': ('collapse',),
            'fields': ('parking', 'cleaning_laundry', 'cleaning_housekeeping'),
        }),
    )

# admin.site.register(Unit)
admin.site.register(Unit, UnitAdmin)
# admin.site.register(Facility)
admin.site.register(Facility, FacilityAdmin)

# only for superuser
# admin.site.register(Language)
# admin.site.register(Bed)


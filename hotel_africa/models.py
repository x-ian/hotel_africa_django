from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=100)
    arrival = models.TextField(max_length=1024, blank=True, default='')
    address_street_1 = models.CharField(max_length=100)
    address_street_2 = models.CharField(max_length=100, blank=True, default='')
    address_city = models.CharField(max_length=100)
    address_zip = models.CharField(max_length=100, blank=True, default='')
    address_state = models.CharField(max_length=100, blank=True, default='')
    address_country = models.CharField(max_length=100)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_long = models.DecimalField(max_digits=9, decimal_places=6)
    contact_email = models.EmailField(max_length=100)
    contact_phone_1 = models.CharField(max_length=100)
    contact_phone_2 = models.CharField(max_length=100, blank=True, default='')
    policies = models.TextField(max_length=1024, blank=True, default='')
    directions = models.TextField(max_length=1024, blank=True, default='')
    speciality_beach = models.BooleanField(blank=True)
    speciality_swimming_pool = models.BooleanField(blank=True)
    speciality_fitness_room = models.BooleanField(blank=True)
    speciality_bar = models.BooleanField(blank=True)
    speciality_restaurant_meal_breakfast = models.BooleanField(blank=True)
    speciality_restaurant_meal_dinner = models.BooleanField(blank=True)
    speciality_restaurant_meal_lunch = models.BooleanField(blank=True)
    speciality_restaurant_prices = models.TextField(max_length=1024, blank=True, default='')
    speciality_restaurant_times = models.TextField(max_length=1024, blank=True, default='')
    speciality_kids_playground = models.BooleanField(blank=True)
    speciality_airport_shuttle = models.BooleanField(blank=True)
    speciality_24h_front_desk = models.BooleanField(blank=True)
    speciality_extras = models.TextField(max_length=1024, blank=True, default='')
    parking = models.BooleanField(blank=True)
    cleaning_laundry = models.BooleanField(blank=True)
    cleaning_housekeeping = models.BooleanField(blank=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100) 
    
    facility = models.ForeignKey(
        Facility, 
        on_delete=models.DO_NOTHING,
    )
    
    quantity_of_units_in_facility = models.IntegerField()
    class Kind(models.TextChoices):
        ROOM = 'room'
        APARTMENT = 'apartment'
        HOUSE = 'house'
        OTHER = 'other'
    kind = models.CharField(
        max_length=9,
        choices=Kind.choices,
        default=Kind.ROOM,
    )
    max_people = models.IntegerField(null=True, blank=True)
    square_meters = models.IntegerField(null=True, blank=True)
    class InternetAccess(models.TextChoices):
        NO = 'no'
        IN_UNIT = 'in_unit'
        IN_SHARED_AREA = 'in_shared_area'
        UPON_REQUEST = 'upon_request'
    internet_access = models.CharField(
        max_length=14,
        choices=InternetAccess.choices,
        blank=True,
    )
    internet_free_of_charge = models.BooleanField(blank=True)
    furnishing_sitting_area = models.BooleanField(blank=True)
    furnishing_sofa = models.BooleanField(blank=True)
    furnishing_desk = models.BooleanField(blank=True)
    furnishing_extras = models.TextField(max_length=1024, blank=True, default='')
    amenity_ac = models.BooleanField(blank=True)
    amenity_fan = models.BooleanField(blank=True)
    amenity_tv = models.BooleanField(blank=True)
    amenity_private_bathroom = models.BooleanField(blank=True)
    amenity_shower = models.BooleanField(blank=True)
    amenity_towels = models.BooleanField(blank=True)
    amenity_mosquito_net = models.BooleanField(blank=True)
    amenity_private_entry = models.BooleanField(blank=True)
    amenity_smoking = models.BooleanField(blank=True)
    amenity_pets = models.BooleanField(blank=True)
    amenity_wheelchair = models.BooleanField(blank=True)
    amenity_extras = models.TextField(max_length=1024, blank=True, default='')
    views = models.TextField(max_length=1024, blank=True, default='') #has_many

    def __str__(self):
        return self.name

# class FacilityUnit(models.Model):
#     facility = models.ForeignKey(
#         Facility,
#         on_delete=models.DO_NOTHING,
#     )
#     unit = models.ForeignKey(
#         Unit,
#         on_delete=models.DO_NOTHING,
#     )
#     quantity = models.IntegerField()
#
#     def __str__(self):
#         return self.facility.name + "-" + self.unit.name + "-" + str(self.quantity)
#

def upload_facilityphoto_path_handler(instance, filename):
    return "facility_{id}_{name}/facility/{file}".format(id=instance.facility.id, name=instance.facility.name, file=filename)

class FacilityPhoto(models.Model):
    facility = models.ForeignKey(
        Facility, 
        on_delete=models.CASCADE,
    )
    # image = models.ImageField()
    image = models.ImageField(upload_to=upload_facilityphoto_path_handler)

def upload_unitphoto_path_handler(instance, filename):
    return "facility_{id}_{name}/units/{file}".format(id=instance.unit.facility.id, name=instance.unit.facility.name, file=filename)

class FacilityLanguage(models.Model):
    facility = models.ForeignKey(
        Facility, 
        on_delete=models.CASCADE,
    )
    class Languages(models.TextChoices):
        DE = 'german'
        FR = 'french'
        EN = 'english'
        ES = 'spanish'
    language = models.CharField(
        max_length=25,
        choices=Languages.choices,
        blank=False,
    )

class UnitPhoto(models.Model):
    unit = models.ForeignKey(
        Unit, 
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to=upload_unitphoto_path_handler)

class UnitBed(models.Model):
    unit = models.ForeignKey(
        Unit, 
        on_delete=models.CASCADE,
    )
    class BedType(models.TextChoices):
        SINGLE = 'single'
        DOUBLE = 'double'
        KING = 'king'
        OTHER = 'other'
    bed = models.CharField(
        max_length=14,
        choices=BedType.choices,
        blank=False,
    )

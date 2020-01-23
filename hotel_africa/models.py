from django.contrib.auth import get_user_model
from django.db import models
import datetime
import uuid
    
class Facility(models.Model):
    name = models.CharField(max_length=100)
    checkin_from = models.TimeField()
    checkin_to = models.TimeField()
    checkout_from = models.TimeField()
    checkout_to = models.TimeField()
    arrival = models.TextField(max_length=1024, blank=True, default='')
    description = models.TextField(max_length=1024, blank=True, default='')
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

class UnitRate(models.Model):
    name = models.CharField(max_length=100) 
    valid_from = models.DateField()
    valid_to = models.DateField()
    class Currency(models.TextChoices):
        USD = 'USD (USA)'
        EUR = 'EUR (Europe)'
        XOF = 'XOF (CFA Franc)'
        NGN = 'NGN (Nigeria)'
        MWK = 'MWK (Malawi)'
    rate_currency = models.CharField(
        max_length=25,
        choices=Currency.choices,
        default=Currency.USD,
    )
    rate_standard = models.DecimalField(max_digits=6, decimal_places=2)
    rate_early_booker = models.DecimalField(max_digits=6, decimal_places=2)
    free_cancellation = models.BooleanField(default=False)
    rate_cancellation = models.DecimalField(max_digits=6, decimal_places=2)
    payment_cash = models.BooleanField(default=False)
    payment_creditcard = models.BooleanField(default=False)
    payment_paypal = models.BooleanField(default=False)
    payment_wiretransfer = models.BooleanField(default=False)
    payment_westernunion = models.BooleanField(default=False)
    special_offers = models.TextField(max_length=1024, blank=True, default='')
    meals = models.TextField(max_length=1024, blank=True, default='')

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField(max_length=1024, blank=True, default='')
    
    facility = models.ForeignKey(Facility, on_delete=models.DO_NOTHING,)
    
    quantity_of_units_in_facility = models.IntegerField()
    class Type(models.TextChoices):
        ROOM = 'room'
        APARTMENT = 'apartment'
        HOUSE = 'house'
        OTHER = 'other'
    type = models.CharField(
        max_length=9,
        choices=Type.choices,
        default=Type.ROOM,
    )
    max_people = models.IntegerField(null=True, blank=True)
    square_meters = models.IntegerField(null=True, blank=True)
    unitrates = models.ManyToManyField(UnitRate)
    
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

class Booking(models.Model):
    booking_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    unit = models.ForeignKey(
        Unit, 
        on_delete=models.DO_NOTHING,
    )
    number_of_persons = models.IntegerField()
    unitrate = models.ForeignKey(
        UnitRate, 
        on_delete=models.DO_NOTHING,
    )
    class StatusType(models.TextChoices):
        NONE = 'None'
        BOOKED = 'Booked'
        CANCELED = 'Canceled'
        NO_SHOW = 'No show'
        COMPLETED = 'Completed'
    status = models.CharField(
        max_length=25,
        choices=StatusType.choices,
        default=StatusType.NONE,
    )
    class PaymentType(models.TextChoices):
        CASH = 'Cash'
        CREDITCARD = 'Credit Card'
        PAYPAL = 'Paypal'
        WIRE_TRANSFER = 'Wire transfer'
        WESTERN_UNION = 'Western Union'
    payment = models.CharField(
        max_length=25,
        choices=PaymentType.choices,
    )
    class Currency(models.TextChoices):
        USD = 'USD (USA)'
        EUR = 'EUR (Europe)'
        XOF = 'XOF (CFA Franc)'
        NGN = 'NGN (Nigeria)'
        MWK = 'MWK (Malawi)'
    total_price_currency = models.CharField(
        max_length=25,
        choices=Currency.choices,
        default=Currency.USD,
        editable=False
    )
    total_price = models.DecimalField(default=-1, editable=False, max_digits=6, decimal_places=2)
    
    def __str__(self):
        return str(self.booking_number)

class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.DO_NOTHING, )
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    review_date = models.DateTimeField(auto_now_add=True)
    review_text = models.TextField(max_length=1024, blank=True, default='')
    class Rating(models.TextChoices):
        ONE = '1/5'
        TWO = '2/5'
        THREE = '3/5'
        FOUR = '4/5'
        FIVE = '5/5'
    review_rating = models.CharField(
        max_length=5,
        choices=Rating.choices,
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
    
    def __str__(self):
        return str(self.id)

class Message(models.Model):
    message_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=2048, blank=False)
    from_user = models.ForeignKey(get_user_model(), related_name='from_user', on_delete=models.DO_NOTHING,)
    to_user = models.ForeignKey(get_user_model(), related_name='to_user', on_delete=models.DO_NOTHING)
    refer_booking = models.ForeignKey(Booking, blank=True, on_delete=models.DO_NOTHING)
    refer_unit = models.ForeignKey(Unit, blank=True, on_delete=models.DO_NOTHING)
    refer_facility = models.ForeignKey(Facility, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

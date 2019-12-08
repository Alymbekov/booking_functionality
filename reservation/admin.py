from django.contrib import admin
from .models import Reservation, Table, Customer


admin.site.register(Reservation)
admin.site.register(Table)
admin.site.register(Customer)


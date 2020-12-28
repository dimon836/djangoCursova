from django.contrib import admin
from .models import CompanyDB, Month, ProductionRate, PositionEm, HistoryPromotions, WorkingMachine, OilChange, \
    MachineBreakdowns, Subdivision, TableSheet, Employer, Trip, Vacation, Coupon, HospitalTrip


admin.site.register(CompanyDB)
admin.site.register(Month)
admin.site.register(ProductionRate)
admin.site.register(PositionEm)
admin.site.register(HistoryPromotions)
admin.site.register(Coupon)
admin.site.register(WorkingMachine)
admin.site.register(OilChange)
admin.site.register(MachineBreakdowns)
admin.site.register(Subdivision)
admin.site.register(TableSheet)
admin.site.register(Employer)
admin.site.register(Trip)
admin.site.register(HospitalTrip)
admin.site.register(Vacation)

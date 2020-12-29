from django.db import models


class Month(models.Model):
    name = models.CharField('Name', max_length=20)
    num_of_workday = models.IntegerField("Number of workdays")


class ProductionRate(models.Model):
    det_per_hour = models.IntegerField('Detail per hour')
    amount_h = models.IntegerField("Amount hour")


class PositionEm(models.Model):
    name = models.CharField('Name', max_length=64)
    date_up = models.DateField()
    id_rate = models.ForeignKey('ProductionRate', on_delete=models.PROTECT)


class HistoryPromotions(models.Model):
    name = models.CharField('Name status', max_length=64)
    date_up = models.DateField()


class Coupon(models.Model):
    type_of_transport = models.CharField('Type of transport', max_length=64)
    cost_road = models.IntegerField('Price of road')
    cost_housing = models.IntegerField('Price of housing')


class WorkingMachine(models.Model):
    name = models.CharField('Name machine', max_length=64)
    model = models.CharField('Model machine', max_length=64)
    year_creation = models.IntegerField('Year creation')


class OilChange(models.Model):
    amount_oil = models.IntegerField('Year creation')
    date_change = models.DateField()
    id_machine = models.ForeignKey('WorkingMachine', on_delete=models.PROTECT)


class MachineBreakdowns(models.Model):
    date_breakdown = models.DateField()
    num_breakdown = models.IntegerField('Number breakdowns')
    cost = models.IntegerField('Costs')
    id_machine = models.ForeignKey('WorkingMachine', on_delete=models.PROTECT)


class Subdivision(models.Model):
    name = models.CharField('Name subdivision', max_length=64)
    id_machine = models.ForeignKey('WorkingMachine', on_delete=models.PROTECT)


class TableSheet(models.Model):
    id_employer = models.ForeignKey('Employer', on_delete=models.PROTECT)
    id_month = models.ForeignKey('Month', on_delete=models.PROTECT)
    nhd = models.IntegerField("Amount of hospital days")
    ntd = models.IntegerField("Amount of trip days")
    nvd = models.IntegerField("Amount of vacation days")


class Employer(models.Model):
    name = models.CharField('Name', max_length=64)
    surname = models.CharField('Surname', max_length=64)
    last_name = models.CharField('Last name', max_length=64)
    id_subdivision = models.ForeignKey('Subdivision', on_delete=models.PROTECT)
    id_status = models.ForeignKey('HistoryPromotions', on_delete=models.PROTECT)
    id_position = models.ForeignKey('PositionEm', on_delete=models.PROTECT)


class Trip(models.Model):
    date = models.DateField("Date of trip")
    location = models.CharField("Location", max_length=64)
    num_days = models.IntegerField('Amount of days')
    id_talon = models.ForeignKey('Coupon', on_delete=models.PROTECT)
    id_employer = models.ForeignKey('Employer', on_delete=models.PROTECT)


class HospitalTrip(models.Model):
    date_start = models.DateField("Date start")
    disease = models.CharField("Disease", max_length=64)
    num_days = models.IntegerField('Amount of days')
    id_employer = models.ForeignKey('Employer', on_delete=models.PROTECT)


class Vacation(models.Model):
    date_start = models.DateField("Date start")
    num_days = models.IntegerField('Amount of days')
    id_employer = models.ForeignKey('Employer', on_delete=models.PROTECT)

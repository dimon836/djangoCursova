from django.db import models


class CompanyDB(models.Model):
    title = models.CharField('Name', max_length=40)
    task = models.TextField('Description')


class Coupon(models.Model):
    type_of_transport = models.CharField('TypeOfTransport', max_length=64)
    cost_road = models.IntegerField('RoadCost')
    cost_housing = models.IntegerField('AccommodationCost')

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

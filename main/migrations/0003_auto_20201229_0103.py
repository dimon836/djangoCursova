# Generated by Django 3.1.4 on 2020-12-28 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_coupon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'Купон', 'verbose_name_plural': 'Купоны'},
        ),
        migrations.CreateModel(
            name='HospitalTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coupon')),
            ],
        ),
    ]

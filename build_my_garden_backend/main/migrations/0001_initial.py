# Generated by Django 4.0.5 on 2022-07-01 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=200)),
                ('plant_type', models.CharField(max_length=200)),
                ('plant_size_height', models.IntegerField()),
                ('plant_size_spread', models.IntegerField()),
                ('plant_max_size_time', models.DurationField()),
                ('plant_harvest_length', models.DurationField()),
                ('sun_exposer', models.CharField(choices=[('FULL_SUN', 'Full Sunlight'), ('PARTIAL_SUN', 'Partial Sunlight'), ('PARTIAL _OR_FULL_SUN', 'Full Sunlight or Partial Sunlight')], default='PARTIAL _OR_FULL_SUN', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(choices=[('FALL', 'Fall'), ('WINTER', 'Winter'), ('SPRING', 'Spring'), ('SUMMER', 'Summer')], default='SPRING', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SoilType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil_name', models.CharField(max_length=200)),
                ('soil_description', models.TextField(max_length=200)),
                ('soil_degradation_duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil_current_degradation', models.FloatField()),
                ('account_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soil_account', to=settings.AUTH_USER_MODEL)),
                ('soil_type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soil_type', to='main.soiltype')),
            ],
        ),
        migrations.CreateModel(
            name='PlantSupportingSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plant_supporting_season', to='main.planttype')),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plant_supporting_season', to='main.season')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_current_size_height', models.IntegerField()),
                ('plant_current_size_spread', models.IntegerField()),
                ('planted_date', models.DateTimeField()),
                ('plant_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plant', to='main.planttype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

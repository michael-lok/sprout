# Generated by Django 4.0.6 on 2022-07-29 03:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planttracker', '0003_rename_plant_id_possession_plant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='possession',
            name='days_fertilize',
            field=models.IntegerField(blank=True, help_text='frequency in which plant should be fertilized', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='days between fertilization'),
        ),
        migrations.AlterField(
            model_name='possession',
            name='days_repot',
            field=models.IntegerField(blank=True, help_text='frequency in which plant should be repotted', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='days between repotting'),
        ),
        migrations.AlterField(
            model_name='possession',
            name='days_water',
            field=models.IntegerField(blank=True, help_text='frequency in which plant should be watered', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='days between watering'),
        ),
        migrations.AlterField(
            model_name='possession',
            name='sprouter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('AQ', 'Acquired'), ('WT', 'Watered'), ('FZ', 'Fertilized'), ('RP', 'Repotted')], max_length=20)),
                ('activity_date', models.DateField(default=django.utils.timezone.now, help_text='date in which activity took place.')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('posession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planttracker.possession')),
            ],
        ),
    ]
from django.db import migrations, models
import django.db.models.deletion
from django.db.transaction import atomic

from django_weekend.models import Days


@atomic
def create_setting_and_fill_days_names(apps, schema_editor):
    setting_model = apps.get_model('weekends', 'CommonWorkingWeekSettings')
    days_model = apps.get_model('weekends', 'Days')
    setting_instance = setting_model.objects.create()
    for day_name in Days.AVAILABLE_DAYS:
        obj = days_model(setting=setting_instance, name=day_name)
        obj.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonWorkingWeekSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date created')),
            ],
            options={
                'verbose_name': 'Common working week setting',
                'verbose_name_plural': 'Common working week settings',
            },
        ),
        migrations.CreateModel(
            name='ExcludedWeekends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date created')),
                ('date', models.DateField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Excluded weekend',
                'verbose_name_plural': 'Excluded weekends',
            },
        ),
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date created')),
                ('date', models.DateField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Holiday',
                'verbose_name_plural': 'Holidays',
            },
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9, verbose_name='Day name')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='weekends.commonworkingweeksettings', verbose_name='Setting')),
            ],
            options={
                'verbose_name': 'Week day',
                'verbose_name_plural': 'Week days',
            },
        ),
        migrations.RunPython(create_setting_and_fill_days_names),
    ]

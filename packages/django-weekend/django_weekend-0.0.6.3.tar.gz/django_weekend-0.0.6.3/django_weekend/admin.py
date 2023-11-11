from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Holidays, ExcludedWeekends, CommonWorkingWeekSettings, Days


class DaysFormAdmin(forms.ModelForm):
    class Meta:
        model = Days
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name and name not in Days.AVAILABLE_DAYS:
            raise ValidationError(f'Not available day name. Available: {", ".join(Days.AVAILABLE_DAYS)}')
        return cleaned_data


class InlineDaysAdmin(admin.TabularInline):
    model = Days
    extra = 1
    can_delete = True
    form = DaysFormAdmin


@admin.register(Holidays)
class HolidaysAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    date_hierarchy = 'date'


@admin.register(ExcludedWeekends)
class ExcludedWeekendsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')
    date_hierarchy = 'date'


@admin.register(CommonWorkingWeekSettings)
class CommonWorkingWeekSettingsAdmin(admin.ModelAdmin):
    inlines = (InlineDaysAdmin,)

    # TODO Если переделывать что бы настройки были для каждого пользователя, то переопределить этот метод,
    # потому что может быть несколько настроек для каждого пользователя
    def has_add_permission(self, request):
        is_has_perms = super().has_add_permission(request)
        if not is_has_perms:
            return False
        return not CommonWorkingWeekSettings.objects.exists()
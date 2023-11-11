from django.db.models import Model, DateField, CharField, ForeignKey, CASCADE


class AbstractCreatedModel(Model):
    date_created = DateField(verbose_name='Date created', auto_now_add=True, editable=False)

    class Meta:
        abstract = True
        ordering = ('-date_created',)


class AbstractDateModel(AbstractCreatedModel):
    date = DateField(verbose_name='Date')

    class Meta:
        abstract = True

    def __str__(self):
        return f'ID: {self.id} | Date: {self.date}'


class Holidays(AbstractDateModel):
    class Meta:
        verbose_name = 'Holiday'
        verbose_name_plural = 'Holidays'


class ExcludedWeekends(AbstractDateModel):
    class Meta:
        verbose_name = 'Excluded weekend'
        verbose_name_plural = 'Excluded weekends'


class CommonWorkingWeekSettings(AbstractCreatedModel):
    class Meta:
        verbose_name = 'Common working week setting'
        verbose_name_plural = 'Common working week settings'

    def __str__(self) -> str:
        return f'Common working week setting | ID: {self.id}'


class Days(Model):
    AVAILABLE_DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    setting = ForeignKey(CommonWorkingWeekSettings, on_delete=CASCADE, verbose_name='Setting', related_name='days')
    name = CharField(verbose_name='Day name', max_length=9)

    class Meta:
        verbose_name = 'Week day'
        verbose_name_plural = 'Week days'

    def __str__(self):
        return f'ID: {self.id} | Name: {self.name} | Setting: {self.setting}'
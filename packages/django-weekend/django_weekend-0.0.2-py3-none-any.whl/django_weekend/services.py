import datetime
from typing import List

from .models import Holidays, ExcludedWeekends, CommonWorkingWeekSettings


class HolidaysWeekendsService:
    def __init__(self) -> None:
        self.working_week_settings = CommonWorkingWeekSettings.objects.first()
        if not self.working_week_settings:
            raise ValueError('Common working week settings not found. Make sure this is exist.')

    def _is_holiday(self, date: datetime.date) -> bool:
        return Holidays.objects.filter(date=date).exists()

    def _is_excluded_weekend(self, date: datetime.date) -> bool:
        return ExcludedWeekends.objects.filter(date=date).exists()

    def _get_day_name(self, date: str) -> str:
        return date.strftime('%A')

    def _is_weekend(self, day: str) -> bool:
        return not self.working_week_settings.days.filter(name=day).exists()

    def _get_dates_range(self, start_date: str, end_date: str) -> List[str]:
        """
            Generate a list of dates between start_date and end_date.
            Args:
                start_date (str): The start date in the format 'YYYY-MM-DD'.
                end_date (str): The end date in the format 'YYYY-MM-DD'.
            Returns:
                List[str]: A list of dates between start_date and end_date in the format 'YYYY-MM-DD'.
        """
        dates_range = []
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        current_date = start_date_obj
        while current_date <= end_date_obj:
            dates_range.append(current_date)
            current_date += datetime.timedelta(days=1)

        return [date.strftime('%Y-%m-%d') for date in dates_range]

    def is_weekend_by_date(self, date: str) -> bool:
        """
            Determines if a given date is a weekend or a holiday.

            Args:
                date (str): The date in the format 'YYYY-MM-DD'.

            Returns:
                bool: True if the date is a weekend or a holiday, False otherwise.
        """
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        date_name = self._get_day_name(date=date_obj)
        is_weekend = self._is_weekend(day=date_name)
        is_excluded_weekend = self._is_excluded_weekend(date=date_obj)
        is_holiday = self._is_holiday(date=date_obj)
        is_weekend = is_weekend and not is_excluded_weekend

        return is_weekend or is_holiday

    def get_weekends_by_range(self, start_date: str, end_date: str) -> List[str]:
        """
            Returns a list of weekend dates between the given start_date and end_date.

            Args:
                start_date (str): The start date in the format 'YYYY-MM-DD'.
                end_date (str): The end date in the format 'YYYY-MM-DD'.

            Returns:
                List[str]: A list of weekend dates in the format 'YYYY-MM-DD'.
        """
        dates_range = self._get_dates_range(start_date=start_date, end_date=end_date)
        return [date for date in dates_range if self.is_weekend_by_date(date=date)]
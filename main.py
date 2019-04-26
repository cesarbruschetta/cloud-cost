from datetime import date
from calendar import monthrange

PRICE_QUEUE = 0.00000040
PRICE_EXECUTION = 0.0000002
PRICE_BY_SECOND_EXECUTION = 0.0002080
TIME_EXECUTION = 3.0
COUNT_FUNCTION = 2.0


class CloudCost:
    def _days_in_month(self, month):
        _date = date.today()
        _, days_month = monthrange(_date.year, month)
        return days_month

    def lambda_execution(self):
        return (PRICE_BY_SECOND_EXECUTION * TIME_EXECUTION) + PRICE_EXECUTION

    def app_execution(self, execution_times):
        return (
            (self.lambda_execution() * COUNT_FUNCTION) + PRICE_QUEUE
        ) * execution_times

    def month(self, execution_times, month_of_year):
        _days = self._days_in_month(month_of_year)
        return self.app_execution(execution_times) * _days

    def year(self, execution_times):
        data = [self.month(execution_times, month) for month in range(1, 13)]
        return data

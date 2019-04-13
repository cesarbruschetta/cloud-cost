from decimal import Decimal
from datetime import date
from calendar import monthrange

from constants import *


class CloudCost:
    def _days_in_month(self, month):

        _date = date.today()
        _, days_month = monthrange(_date.year, month)
        return days_month

    def float2decimal(self, float):
        return Decimal(float)

    def decimal2float(self, decimal):
        return float(
            "{:f}".format(decimal)
        )

    def lambda_execution(self):
        
        _price = (PRICE_BY_SECOND_EXECUTION * TIME_EXECUTION) + PRICE_EXECUTION
        return self.decimal2float(_price)

    def app_execution(self, execution_times):

        price = (
            self.float2decimal(self.lambda_execution()) * COUNT_FUNCTION
        ) + PRICE_QUEUE
        total = price * execution_times
        return self.decimal2float(total)

    def month(self, execution_times, month_of_year):

        _days = self._days_in_month(month_of_year)
        cost_month = self.float2decimal(self.app_execution(execution_times)) * _days
        return self.decimal2float(cost_month)

    def year(self, execution_times):

        data = []
        for month in range(1, 13):
            data.append(self.month(execution_times, month))
        return data

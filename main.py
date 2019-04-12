
from datetime import date
from calendar import monthrange, month_abbr

from constants import *


class CloudCost():
    
    def _days_in_month(self, month):

        _date = date.today()
        _, days_month = monthrange(_date.year, month)
        return days_month

    def lambda_execution(self):

        return PRICE_EXECUTION * TIME_EXECUTION

    def app_execution(self, execution_times):

        price = (self.lambda_execution() * COUNT_FUNCTION) + PRICE_QUEUE
        return price * execution_times


    def month(self, execution_times, month_of_year):

        _days = self._days_in_month(month_of_year)
        cost_month = self.app_execution(execution_times) * _days
        return cost_month
    
    def year(self, execution_times):
        
        data = []
        for month in range(1, 13):
            data.append({
                'month': month,
                "month_abbr": month_abbr[month],
                "cost_month": self.month(execution_times, month)
            })
        return data

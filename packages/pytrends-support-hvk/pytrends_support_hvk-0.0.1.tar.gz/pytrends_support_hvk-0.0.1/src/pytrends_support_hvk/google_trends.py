from pytrends.request import TrendReq
import pandas as pd
import datetime as dt
from datetime import timedelta

#----Class---#
class Google:

    def __init__ (self, kw_list, days):
        self.kw_list = kw_list
        self.days=days

    def today(self):
        self.raw_today = dt.datetime.now()
        self.today = self.raw_today.strftime('%Y-%m-%d')
        return self.today

    def start (self):
        self.raw_today = dt.datetime.now()
        self.start_date = (self.raw_today - timedelta(days=self.days)).strftime('%Y-%m-%d')
        return self.start_date

    def trends(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)
        self.pytrends.build_payload([self.kw_list], cat=0, timeframe=f'{self.start()} {self.today()}', geo='US', gprop='')
        self.trends = self.pytrends.interest_over_time()
        self.df = pd.DataFrame(self.trends)
        return self.df


#----TEST CODE---#
# kw_list = "python"
# days = 150
# google_trends = Google (kw_list, days)
# google_trends.trends().to_csv('google_trends.csv', index=True)


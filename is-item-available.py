"""
1.Function to find if a menu item is available at the moment or not

A menu item ( eg: Dosa ) in a restaurant menu is available during certain period of time
in a day. For example Dosa might be available from 7:00 to 10:00 and from 17:00 to
21:00. Objective of the program is to find out if this item is currently available or not
based on the system time.


Implement a function called ‘IsItemAvailable’ which accepts ‘itemname’ and ‘timestring’
as parameters and returns yes or no based on current
Input:
itemname = 'Dosa'
timestring = '

Output:
If current time is 17:15
Dosa available
if current time is 12:30
Dosa not available
================================================================================================================
1. GET -> receive current_time. Response -> send cookie with the same current_time
2. POST -> request: {itemname: '', timestring: ''}. Pick cookie and call method. Response {"message": "Dosa .."}
"""

import datetime


class Restutant:
    now = datetime.datetime.now()
    current_time = datetime.timedelta(hours=now.hour, minutes=now.minute)

    def __init__(self, itemname: str, timestring: str):
        self.itemname = itemname
        self.timestring = timestring

    @staticmethod
    def _str_to_time_obj(time):
        try:
            new_time = datetime.timedelta(hours=int(time.split(':')[0]), minutes=int(time.split(':')[1]))
        except Exception as e:
            print(e)
            return None
        else:
            return new_time

    @staticmethod
    def _str_to_time_string(time):
        return list(time.split(','))

    def is_item_available(self):
        for item in self._str_to_time_string(self.timestring):        
            strat_time = self._str_to_time_obj(item.split('-')[0])
            end_time = self._str_to_time_obj(item.split('-')[1])
            if strat_time <= self.current_time < end_time:
                print(f"{self.itemname} time: {strat_time}-{end_time}")
                return True
            print(f"{strat_time}-{end_time} No {self.itemname}")
        return False


ITEM_NAME = "Dosa"
TIMESTRING = "16:00-17:00,7:00-10:00,17:00-21:00"


r = Restutant(ITEM_NAME, TIMESTRING)
print(r.is_item_available())

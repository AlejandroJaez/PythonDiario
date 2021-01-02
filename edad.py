
"""
A widget showing the current time.
"""

import widgets as wd
from datetime import time, date, datetime
import datetime as dt


BACKGROUND = wd.Color.rgb(255/255, 250/255, 227/255)
FOREGROUND = wd.Color.rgb(75/255, 72/255, 55/255)

class TimeProvider(wd.TimelineProvider):
    
    def widget(self, dates):
        widget = wd.Widget()
        b = date(1992, 6, 16)
        until30 = dt.date(2022,6,16) - dt.date.today()
        now = dates.time()
        hour = wd.Text(
        text=str(until30.days)+"dias",
        font=wd.Font("AmericanTypewriter-Bold", 50),
        color=FOREGROUND,
        )
        
        minutes = wd.DynamicDate(
            date=time(now.hour, 0, 0),
            style=wd.DATE_STYLE_RELATIVE,
            font=wd.Font("AmericanTypewriter", 17),
            color=FOREGROUND,
            padding=wd.PADDING_ALL
        )

        layouts = [widget.small_layout, widget.medium_layout]
        for layout in layouts:
            
            layout.add_vertical_spacer()
            layout.add_row([hour])
            layout.add_row([minutes])
            layout.set_background_color(BACKGROUND)
    
        return widget
    
    def timeline(self):
        
        today = date.today()
        dates = []
        for i in range(24):
            now = time(i, 0, 0)
            current_date = datetime.combine(today, now)
            dates.append(current_date)
        
        return dates

wd.provide_timeline(TimeProvider())


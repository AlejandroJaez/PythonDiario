import datetime as dt

def DiasParaLos30s():
        # Number of dates
        until30 = dt.date(2022,6,16) - dt.date.today()
        return until30.days

print(DiasParaLos30s())
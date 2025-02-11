import datetime
today = datetime.date.today()
vday = datetime.date(2025,2,14)
diff = vday-today
meow = diff.days
hours = (meow*24)
print (hours)

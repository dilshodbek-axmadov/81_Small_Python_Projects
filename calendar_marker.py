import datetime
from pathlib import Path

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

def validate_year():
    while True:
        year = input("Enter the year for the calendar:\n> ")
        if not year.isdecimal():
            continue
        year = int(year)
        if year<0:
            print("Enter valid year")
            continue
        else:
            return year

def validate_month():
    while True:
        month = input("Enter the month for the calendar, 1-12:\n> ")
        if not month.isdecimal():
            continue
        month = int(month)
        if 1<=month<=12:
            return month
        else:
            print("Invalid month!")


def get_calendar_for(year, month):
    first_day_of_month = datetime.date(year, month,1)

    calText = ''
    calText += ('  '*8) + MONTHS[month-1] + ' ' + str(year) + '\n'
    calText += ' Sunday   Monday     Tuesday   Wednesday Thursday  Friday   Saturday\n'
    weekSeparator = ('+---------'*7) + '+\n'
    blank_row = ('|         '*7) + '|\n'
    while first_day_of_month.weekday() != 6:
        first_day_of_month -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator
        day_number_row = ''
        for i in range(7):
            day_number_label = str(first_day_of_month.day).rjust(2)
            day_number_row += '|' + day_number_label + ('       '*1)
            first_day_of_month += datetime.timedelta(1)
        day_number_row += '|\n'

        calText += day_number_row
        for i in range(3):
            calText += blank_row

        if first_day_of_month.month != month:
            break
    calText += weekSeparator
    return calText

year_ = validate_year()
month_ = validate_month()

calendar_for_month = get_calendar_for(year_, month_)
print(calendar_for_month)

# Folder path
folder_path = Path("calendar")

# Define filename
calendar_filename = f'calendar_{year_}_{month_}.txt'
# Full path
full_path = folder_path/calendar_filename

# Create calendar folder if it does not exist
folder_path.mkdir(parents=True, exist_ok=True)

with open(full_path,'w') as obj:
    obj.write(calendar_for_month)

print('Saved to ' + calendar_filename)
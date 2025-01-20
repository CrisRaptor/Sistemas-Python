def is_year_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month > 0 and month < 13:
        if month == 2:
            if is_year_leap(year):
                return 29
            return 28
        if month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        return 31
    return -1

def day_of_year(year, month, day):
    total_days = 0
    for counter_month in range(1,month):
        total_days += days_in_month(year, counter_month)
    total_days += day
    return total_days

print(day_of_year(2000, 12, 31))
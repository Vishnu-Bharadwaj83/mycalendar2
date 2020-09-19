# mycalendar2.py
# - a calendar of my school schedule on Thursdays and Fridays

def print_calendar(day, format_one, time, format_two, subject):
    print(day+format_one+time+format_two+subject)
    
day = 'Day'
no_day = ''
time = 'Time'
subject = 'Subject'
one_tab ='\t'
two_tabs = '\t\t'
print_calendar(day, two_tabs, time, two_tabs+one_tab, subject)

day = 'Thursday'
time = '9:10 - 10:15'
subject = 'Language Arts'
print_calendar(day, one_tab, time, two_tabs, subject)

time = '10:35 - 11:40'
subject = 'Social Studies'
print_calendar(no_day, two_tabs, time, two_tabs, subject)

time = '12:10 - 1:15'
subject = 'Science'
print_calendar(no_day, two_tabs, time, two_tabs, subject)

day = 'Friday'
time = '9:10 - 10:15'
subject = 'Math'
print_calendar(day, two_tabs, time, two_tabs, subject)

time = '10:35 - 11:40'
subject = 'Exploratory Wheel'
print_calendar(no_day, two_tabs, time, two_tabs, subject)

time = '12:10 - 1:15'
subject = 'Physical Fitness'
print_calendar(no_day, two_tabs, time, two_tabs, subject)

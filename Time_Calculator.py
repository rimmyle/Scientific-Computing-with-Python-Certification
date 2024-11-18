def add_time(start, duration, week=''):
    days = int(duration.split(':')[0]) // 24
    hours = int(start.split(' ')[0].split(':')[0]) + int(duration.split(':')[0]) % 24
    minutes = int(start.split(' ')[0].split(':')[1]) + int(duration.split(':')[1])
    
    if minutes > 60:
        hours += minutes // 60
        minutes = minutes % 60

    if start.split(' ')[1] == 'PM':
        hours += 12

    while hours >= 24:
        hours -= 24
        days += 1

    meridian = 'PM' if hours >= 12 else 'AM'
    
    hours %= 12
    hours = 12 if hours == 0 else str(hours)
    minutes = '0' + str(minutes) if len(str(minutes)) < 2 else str(minutes)
    time = f'{hours}:{minutes} {meridian}'

    if week:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start = days_of_week.index(week.lower().capitalize())
        time += f', {days_of_week[start]}' if days == 0 else f', {days_of_week[(start + days) % 7]}'
        
    if days:
        time += ' (next day)' if days == 1 else f' ({days} days later)'
    
    return time

print( add_time('2:59 AM', '24:00', 'saturDay'))
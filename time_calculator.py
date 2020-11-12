def add_time(start, duration, week_day=None):
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    st_time, meridian = start.split()
    st_hh, st_mm = map(int, st_time.split(':'))
    d_hh, d_mm = map(int, duration.split(':'))

    _mm = st_mm + d_mm
    new_mm = _mm % 60

    _hh = st_hh + d_hh + _mm // 60 + 12 * (meridian == 'PM')
    new_hh = _hh % 24
    if new_hh >= 12:
        if new_hh > 12:
            new_hh -= 12
        new_meridian = 'PM'
    else:
        if new_hh == 0:
            new_hh += 12
        new_meridian = 'AM'

    _days = _hh // 24
    if _days > 1:
        next_days = f' ({_days} days later)'
    elif _days == 1:
        next_days = ' (next day)'
    else:
        next_days = ''

    if week_day:
        print(week_day)
        new_week_day = ', ' + week_days[(_days + week_days.index(week_day.capitalize())) % 7]
    else:
        new_week_day = ''

    new_time = f'{new_hh}:{str(new_mm).zfill(2)} {new_meridian}{new_week_day}{next_days}'
    return new_time
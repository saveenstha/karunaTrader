from datetime import date

def get_season_range(year, season_number):
    if season_number == 1:
        return date(year, 4, 1), date(year, 6, 30)
    elif season_number == 2:
        return date(year, 10, 1), date(year, 12, 31)
    return None, None

def get_available_seasons(start_year=2020):
    current_year = date.today().year
    return [
        (y, s) for y in range(current_year, start_year - 1, -1) for s in [1, 2]
    ]

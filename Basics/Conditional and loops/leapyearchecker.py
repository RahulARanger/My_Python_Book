def is_leap(year_):
    if year_ % 4 == 0:
        if year_ % 100 == 0:
            if year_ % 400 == 0:
                return True
        else:
            return True
    return False


year = int(input())
print(is_leap(year))

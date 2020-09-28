from datetime import datetime


def get_release_date(release_str):
    return datetime.strptime(release_str[release_str.find(':') + 2:], '%d %B %Y')

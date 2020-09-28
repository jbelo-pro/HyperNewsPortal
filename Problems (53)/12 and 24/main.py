from datetime import datetime


def format_time(datetime_obj):
    print('24h {}'.format(datetime_obj.strftime('%H:%M')))
    print('12h {}'.format(datetime_obj.strftime('%I:%M')))

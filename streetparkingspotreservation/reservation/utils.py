from datetime import datetime, timedelta

RESERVATION_COST_PER_HOUR = 100


def get_booking_cost(duration):
    """

    :param duration:
    :return:
    """
    return duration * RESERVATION_COST_PER_HOUR


def get_booking_endtime(booking_start_time =None, duration=1):
    """

    :param booking_start_time:
    :param duration:
    :return:
    """

    return booking_start_time + timedelta(hours=duration)


def get_booking_starttime(booking_from=None):

    return get_date(booking_from["hour"],
                    booking_from["minutes"],
                    booking_from["period"])


def get_date(hour, minutes, period):
    """

    :param hour:
    :param minutes:
    :param period:
    :return:
    """
    today = datetime.today()
    date_string = '{0}-{1}-{2} {3}:{4} {5}'.format(today.year,
                                                   today.month,
                                                   today.day,
                                                   hour,
                                                   minutes,
                                                   period)
    format = '%Y-%m-%d %I:%M %p'
    return  datetime.strptime(date_string, format)
import ast
import datetime


def convert_date(date):
    """
    This method converts a date to american pattern.
    :param date: Date to be converted.
    :return: String Date in american pattern.
    """
    formats = ['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y',
               '%Y/%m/%d', '%Y-%m-%d', '%y/%m/%d', '%y-%m-%d', '%m/%d/%Y']
    for format_date in formats:
        try:
            if not isinstance(date, datetime.datetime):
                date = str(datetime.datetime.strptime(date, format_date).date())
            return date
        except ValueError:
            continue

    raise ValueError


def serialize_dict(dic):
    return repr(dic)


def deserialize_dict(dic):
    return ast.literal_eval(dic)

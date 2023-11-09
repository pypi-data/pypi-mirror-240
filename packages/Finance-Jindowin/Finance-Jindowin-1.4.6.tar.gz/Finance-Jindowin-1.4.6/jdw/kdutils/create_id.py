import dateutil.parser as dt_parser
import time, uuid, math, datetime


def convert_date(date, format='%Y-%m-%d'):
    try:
        unicode
    except:
        unicode = str
    try:
        if isinstance(date, (str, unicode)):
            date = dt_parser.parse(date)
    except Exception as e:
        raise Exception('date:{}格式不能识别。' % date)
    return date.strftime(format)


def string_to_int(string, alphabet):
    number = 0
    alpha_len = len(alphabet)
    for char in string[::-1]:
        number = number * alpha_len + alphabet.index(char)
    return number


def init_bet():
    alphabet = list("0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"
                    "abcdefghijkmnopqrstuvwxyz")
    new_alphabet = list(sorted(set(alphabet)))
    if len(new_alphabet) > 1:
        alphabet = new_alphabet
    return alphabet


def create_id(original=None, digit=8):
    ori_str = original if original is not None else uuid.uuid1().hex[-12:]
    s = string_to_int(ori_str, init_bet())
    return str(int(math.pow(10, digit - 1) + abs(hash(s)) % (10**(digit - 2))))


def create_task_id(digit=10):
    s = str(time.time() * 10e5 + datetime.datetime.now().microsecond)[:-2]
    return create_id(original=s, digit=digit)
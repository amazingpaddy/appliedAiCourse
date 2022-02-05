
class MyException(Exception):
    pass


def get_error(num):
    try:
        print(num)
        result = 10 / num
        return result
    except ZeroDivisionError:
        raise MyException


print(get_error(0))
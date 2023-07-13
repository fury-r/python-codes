def add(num):
    try:
        if num:
            return int(num)+5
        else:
            return 'enter a number'
    except ValueError as err:
        return err
def check(num):
    try:
        return int(num)%2==0
    except ValueError as err:
        return err
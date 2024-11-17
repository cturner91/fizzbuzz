
def fizzbuzz_v1(value: int) -> str:
    # deliberately slow / simple
    result = ''
    if value % 5 == 0 and value % 3 == 0:
        result = 'fizzbuzz'
    elif value % 5 == 0:
        result = 'buzz'
    elif value % 3 == 0:
        result = 'fizz'
    return result


def fizzbuzz_v2(value: int) -> str:
    # early returns
    if value % 5 == 0 and value % 3 == 0:
        return 'fizzbuzz'
    elif value % 5 == 0:
        return 'buzz'
    elif value % 3 == 0:
        return 'fizz'
    return ''


def fizzbuzz_v3(value: int) -> str:
    # nested logic
    if value % 5 == 0:
        if value % 3 == 0:
            return 'fizzbuzz'
        return 'buzz'
    elif value % 3 == 0:
       return 'fizz'
    return ''


def fizzbuzz_v4(value: int) -> str:
    # reversed nested logic (going to have fewer misses for div/3)
    if value % 3 == 0:
        if value % 5 == 0:
            return 'fizzbuzz'
        return 'fizz'
    elif value % 5 == 0:
        return 'buzz'
    return ''


def fizzbuzz_v5(value: int) -> str:
    # removing equality operator
    if not value % 3:
        if not value % 5:
            return 'fizzbuzz'
        return 'fizz'
    elif not value % 5:
        return 'buzz'
    return ''


def fizzbuzz_v5b(value: int) -> str:
    # no equality operator and reverse nested
    if not value % 5:
        if not value % 3:
            return 'fizzbuzz'
        return 'buzz'
    elif not value % 3:
        return 'fizz'
    return ''
       

def fizzbuzz_v6(value: int) -> str:
    # using gt logic - faster?
    if value % 3 > 0:
        if value % 5 > 0:
            return ''
        return 'buzz'
        
    if value % 5 > 0:
        return 'fizz'
    return 'fizzbuzz'
	
def fizzbuzz_v7(value: int) -> str:
    # divmod is probably expensive - let's use more basic operations only
    while value >= 15:
        value -= 15
    if not value:
        return 'fizzbuzz'

    value3 = value
    while value3 >= 3:
        value3 -= 3
    if not value3:
        return 'fizz'

    value5 = value
    while value5 >= 5:
        value5 -= 5
    if not value5:
        return 'buzz'
     
    return ''

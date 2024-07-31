calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string_tuple = (len(string), string.upper(), string.lower())
    return string_tuple


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search:
        return True
    else:
        return False


print(string_info('Oppenheimer'))
print(string_info('Наутилус'))
print(string_info('Winnie'))
print(is_contains('ПЕнтагОн', ['эйФориЯ', 'suNFloWer', 'пентАгОН']))
print(is_contains('OCtobEr', ['autumn', 'Январь','окТябрь']))
print(calls)
calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    return tuple_
def is_contains(string, list_to_search):
    count_calls()
    alarmas = False
    for element in list_to_search:
        if string.lower() in element.lower() or element.lower() in string.lower():
            alarmas = True
    return alarmas

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
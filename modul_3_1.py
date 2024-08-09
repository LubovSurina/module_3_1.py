calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

print(string_info('Capybara'))
print(string_info('Armageddon'))
def is_contains(string, list_to_search):
    count_calls()
    a = False
    for i in list_to_search:
        if string.lower() in i.lower():
            a = True
            break
    return a

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

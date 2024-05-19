DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

# Функция для правильного склонения слова "друзья"
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'

def process_anfisa(question):
    if question == 'сколько у меня друзей?':
        count = len(DATABASE)
        friends_count_str = format_friends_count(count)
        return f'У тебя {friends_count_str}.'
    elif question == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif question == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

def process_friend(name, query):
    if name in DATABASE:
        if query == 'ты где?':
            city = DATABASE[name]
            return f'{name} в городе {city}.'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}.'

def process_query(query):
    name, question = query.split(', ', 1)
    if name == 'Анфиса':
        return process_anfisa(question)
    else:
        return process_friend(name, question)

# Проверка вызовов функции process_query()
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))

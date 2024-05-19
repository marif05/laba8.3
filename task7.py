DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
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

def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        # Вызов функции format_friends_count() для корректного ответа
        friends_count_str = format_friends_count(count)
        return f'У тебя {friends_count_str}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        if ', ' in query:
            name, question = query.split(', ', 1)
            if question == 'ты где?':
                if name in DATABASE:
                    city = DATABASE[name]
                    return f'{name} в городе {city}.'
                else:
                    return f'Я не знаю, где {name}.'
        return '<неизвестный запрос>'

print('Привет, я Анфиса!')
print(process_anfisa('сколько у меня друзей?'))
print(process_anfisa('кто все мои друзья?'))
print(process_anfisa('где все мои друзья?'))
print(process_anfisa('кто виноват?'))
print(process_anfisa('Дима, ты где?'))
print(process_anfisa('Соня, ты где?'))

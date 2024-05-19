DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {count} друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        # Новый блок для обработки вопросов об отдельных друзьях
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
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))
print(process_anfisa('Дима, ты где?'))
print(process_anfisa('Соня, ты где?'))
print(process_anfisa('Анфиса, сколько у меня друзей?'))

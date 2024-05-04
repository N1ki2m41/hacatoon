info = {
    "Робітник_1":{
    "Прізвище": 'Бондаренко. В. Д.',
    'Посада': 'Інженер',
    'Коефіцієнт ефективності': '75%',
    'Назви Останніх проектів': ["Розробка ефективної системи очищення повітря в промисловому середовищі","Створення інноваційного пристрою для збереження енергії у будівництві","Оптимізація виробничих процесів у водній сфері для зменшення впливу на навколишнє середовище"]
    },
"Робітник_2":{
    "Прізвище": 'Афанасьєф. А. В.',
    'Посада': 'Менеджер',
    'Коефіцієнт ефективності': '61%',
    'Назви Останніх проектів': ["Впровадження стратегії управління персоналом для підвищення продуктивності","Розробка програми маркетингу для просування нового продукту на ринку","Оптимізація логістичних процесів для зниження витрат та покращення сервісу доставки"]
    },
"Робітник_3":{
    "Прізвище": 'Пустовий. М. А.',
    'Посада': 'Директор 2 філії',
    'Коефіцієнт ефективності': '78%',
    'Назви Останніх проектів': ["Розширення географії обслуговування та розвиток нових ринків","Впровадження програми підвищення якості обслуговування клієнтів","Оптимізація внутрішніх процесів для підвищення ефективності та зниження витрат"]
    }
}
print('1-назви блоків данних про робітників, 2-інфо про робітника')
choice = input("Номер дії (close-вийти)")
while choice != 'close':
    if choice == '1':
        for element in info:
            print('-', element)
    elif choice == '2':
        answer = input('Який робітник?:')
        if answer in info:
            print(info[answer]['Прізвище'])
            print(info[answer]['Посада'])
            print(info[answer]['Коефіцієнт ефективності'])
            print(info[answer]['Назви Останніх проектів'])
        else:
            print('Робітник відсутній у базі данних')
    choice = input("Номер дії (close-вийти)")

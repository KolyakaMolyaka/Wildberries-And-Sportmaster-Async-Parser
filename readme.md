# Установка
```commandline
git clone https://github.com/KolyakaMolyaka/Wildberries-Async-Parser.git
python -m venv venv
pip install -r requirements.txt
```

# Запуск парсера Wildberries
```commandline
py ./parsers/wb_parser/parser.py
```
- Введите название категории для парсинга (из доступных). Например: "Женщинам".
- Введите название подкатегории для парсинга (из доступных). Например: "Блузки и рубашки".
- Введите кол-во страниц для парсинга (самостоятельно). Например: "2".

### Выходные файлы
Файл в формате JSON. Название зависит от выбранной категории и подкатегории, в случае примера выше: "Женщинам_Блузки и рубашки.json"

### Пример выходного JSON
```
[
    {
        "text": "Это не рубашка а фильм ужасов. Ранее покупала рубашку у этого продавца в размере xs что примечательно на мой М сидела отлично и далеко не в обтяг.. нареканий не было, ткань мягкая и тянется. Сейчас поправилась и решила заказать побольше, сразу L чтоб сидела оверсайз, так как знаю что они у них большемерят. Села то она хорошо но к качеству вопросов более чем много, ткань без намека на эластан, она вообще никак не тянется, хлопок как бумага, жесткий. Петли для пуговиц обработаны отвратительно, нитки торчат из каждой петли, сами пуговицы пришиты так, что торчат нитки потянув за которые пуговица просто отвалится.. вернула это безобразие ПЛАТНО, что печалит еле больше. Качество пошива и используемого материала катастрофически испортилось. Вывод - лучше переплатить но получить достойную вещь которая прослужит долго чем этот бумажно нитковый кусок ткани.",
        "val": 1
    },
    {
        "text": "Честно,мне всё понравилось,торчали нитки в некоторых местах но это норм,ещё очень мало просвечивает.Фотки в этой рубашке оставлю в низу.",
        "val": 5
    },
    {
        "text": "Рубашка по качеству хорошая. Раньше брали такую же. Но сейчас не подошёл размер, слишком оверсайс. В пункте выдачи не приняли, т. к. нет обозначения бренда. Но я же его не обрезала, вы сами его не пришиваете. Прошу помочь с возвратом.",
        "val": 5
    },
    ...
]
```

# Запуск парсера Sportmaster
```commandline
py ./parsers/sp_parser/parser.py
```
- Введите ссылку на каталог для парсинга (самостоятельно). Например: "/catalog/zhenskaya_odezhda/kurtki/".
- Введите кол-во страниц для парсинга (самостоятельно). Например: "2".
### Выходные файлы
Файл в формате JSON. Название зависит от выбранной категории (ссылки), в случае примера выше: "zhenskaya_odezhda-kurtki.json"


### Пример выходного файла
```commandline

    {
        "author": "Пользователь скрыл свои данные",
        "starts": 5,
        "date": "10 октября 2023",
        "comments": [
            {
                "Достоинства": "Не продуваемая удобная"
            },
            {
                "Недостатки": "На рост 158 чуть длинновато, но мне понравилось"
            },
            {
                "Комментарий": "Рекомендую однозначно"
            }
        ],
        "details": [
            {
                "Функциональность": "5.0"
            },
            {
                "Соответствие фото": "5.0"
            },
            {
                "Качество": "5.0"
            },
            {
                "Надежность": "5.0"
            },
            {
                "Частота использования": "Ежедневно"
            },
            {
                "Срок использования": "Меньше месяца"
            }
        ],
        "url": "https://www.sportmaster.ru/product/29310960299/"
    },
    {
        "author": "Пользователь скрыл свои данные",
        "starts": 3,
        "date": "10 октября 2023",
        "comments": [
            {
                "Достоинства": "Цвет приятный, карманы глубокие на замке"
            },
            {
                "Недостатки": "Крой неудобный, по спине широкий, спереди не совсем комфортно - тянет. В ветреную погоду - продувает. Капюшон неудобный - огромный (на слона с большими ушами видимо), сползает на лицо."
            },
            {
                "Комментарий": "В целом - неплохо"
            }
        ],
        "details": [
            {
                "Функциональность": "2.0"
            },
            {
                "Соответствие фото": "5.0"
            },
            {
                "Качество": "4.0"
            },
            {
                "Надежность": "2.0"
            },
            {
                "Частота использования": "Ежедневно"
            },
            {
                "Срок использования": "Меньше месяца"
            }
        ],
        "url": "https://www.sportmaster.ru/product/29310960299/"
    },
    ...
```


